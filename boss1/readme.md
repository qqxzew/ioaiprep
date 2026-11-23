# ── ОСМОТР ──
df.head() / df.tail() / df.shape / df.info() / df.describe()
df.dtypes                         # типы колонок
df["col"].unique()                # все уникальные значения
df["col"].value_counts()          # сколько раз встречается каждое
df.isna().sum()                   # пропуски по колонкам
df.duplicated().sum()             # сколько полных дублей строк

# ── УДАЛЕНИЕ ──
df.drop_duplicates()              # убрать полные дубли
df.dropna(subset=["col"])         # убрать строки, где в col пропуск
df.drop(columns=["col"])          # убрать колонку
df[df["col"] > 5]                 # фильтр
df[df["col"].between(a, b)]       # фильтр по диапазону, концы включены

# ── СТРОКИ (.str) ──
df["col"].str.strip()             # убрать пробелы по краям
df["col"].str.lower() / .upper()
df["col"].str.replace("что", "на что")
df["col"].str.contains("текст")   # True/False

# ── ТИПЫ ──
df["col"].astype(int)             # в число (упадёт, если есть мусор или NaN)
pd.to_numeric(df["col"], errors="coerce")   # в число, мусор → NaN
pd.to_datetime(df["col"], format="%d.%m.%Y")

# ── ЗАПОЛНЕНИЕ ПРОПУСКОВ ──
df["col"].fillna(значение)
df["col"].mean() / .median() / .mode()[0]
df.groupby("g")["col"].transform("median")  # медиана своей группы для каждой строки

# ── ПРЕОБРАЗОВАНИЯ ──
df["col"].map({"a": 1, "b": 2})   # замена по словарю
df["col"].apply(функция)          # своя функция на каждое значение
np.where(условие, если_да, есл
listings["ssd_gb"] = listings["ssd_gb"].str.replace("gb", "")и_нет)
pd.get_dummies(df, columns=["col"])   # one-hot

# ── ГРУППИРОВКИ ──
df.groupby("g")["col"].mean()

# ── СКЛЕЙКА ──
pd.merge(left, right, on="key", how="left")
df.rename(columns={"старое": "новое"})

# ── ДАТЫ ──
df["date"].dt.year / .month / .day_of_week
(pd.Timestamp("2026-11-23") - df["date"]).dt.days   # сколько дней прошло

# ── ВЫХОД ──
df[["col1", "col2"]]              # выбрать колонки в нужном порядке
df.sort_values("col")
df.to_csv("clean.csv", index=False)

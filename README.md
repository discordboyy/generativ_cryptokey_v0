# generativ_cryptokey_v0

Простой инструмент для создания Solana-кошелька и работы с ним прямо из браузера, без установки чего-либо на компьютер — всё запускается в **GitHub Codespaces**.

С помощью этого проекта можно:
- сгенерировать новый Solana-кошелёк (публичный + приватный ключ);
- проверить баланс кошелька;
- отправить SOL на другой адрес;
- посмотреть историю транзакций.

---

## ⚠️ Важно про безопасность

- Приватный ключ (`PRIVATE_KEY`) даёт полный доступ к кошельку и деньгам на нём. **Никому его не показывай и никуда не публикуй.**
- Файл `.env` с ключами не должен попадать в git (не коммить его и не выкладывай публично).
- Все операции выполняются в реальной сети Solana **mainnet** — это не тестовая сеть, транзакции необратимы.

---

## Что понадобится

- Аккаунт на GitHub (Codespaces работает прямо в браузере, ничего скачивать не нужно).

---

## Шаг 1. Создаём Codespace

1. Открой этот репозиторий на GitHub.
<img width="1239" height="769" alt="image" src="https://github.com/user-attachments/assets/3a418d37-3dfa-40e1-8284-898cb3b8c3af" />

2. Нажми на зелёную кнопку **Code**.
<img width="1235" height="767" alt="image" src="https://github.com/user-attachments/assets/eb266081-9be5-49d3-96d5-66818b8340c8" />

3. Перейди на вкладку **Codespaces**.
<img width="988" height="470" alt="image" src="https://github.com/user-attachments/assets/40a5171d-ad26-45db-8022-e9049cec9c45" />

4. Нажми **Create codespace on main**.
<img width="972" height="536" alt="image" src="https://github.com/user-attachments/assets/01636ece-ba80-4cb8-9108-d7d9a78e0477" />

5. Подожди 1–2 минуты, пока Codespace настроится — откроется полноценная среда разработки в браузере.

---

## Шаг 2. Устанавливаем зависимости
<img width="1125" height="677" alt="image" src="https://github.com/user-attachments/assets/8b4afb00-8377-430b-88e0-20298ffc9e30" />


Открой файл `command.txt` — в нём собраны все нужные команды. Выполняй их по очереди в терминале (терминал уже открыт внизу окна Codespace):
<img width="892" height="387" alt="image" src="https://github.com/user-attachments/assets/cdd996af-da92-44f6-9dfc-15294f8f0c86" />


```bash
source .venv/bin/activate
pip install --upgrade --force-reinstall -r requirements.txt
```

Дождись, пока установка зависимостей завершится.
<img width="1354" height="860" alt="image" src="https://github.com/user-attachments/assets/d5a86c2d-7fb5-4bb1-afb8-789a583ff3b7" />


---

## Шаг 3. Создаём кошелёк

### Если у тебя ещё нет своего кошелька

В терминале выполни:
<img width="631" height="107" alt="image" src="https://github.com/user-attachments/assets/ceb80714-6ca0-4034-b75c-7c486c66d49b" />


```bash
python main.py
```

Скрипт сгенерирует новый Solana-кошелёк и выведет:

- **Public Address** — публичный адрес кошелька;
- **Private Key** — приватный ключ.

Скопируй оба значения — они понадобятся на следующем шаге.

### Если у тебя уже есть готовый кошелёк

Просто пропусти этот шаг — используй свои существующие ключи на шаге 4.

---

## Шаг 4. Заполняем файл .env
<img width="706" height="347" alt="image" src="https://github.com/user-attachments/assets/05d8e8fb-95d1-48dc-8e9f-5cabea3e68b2" />


1. Создай в корне проекта файл `.env` (если его ещё нет).
2. Вставь туда свои ключи в таком виде:

```dotenv
PUBLIC_KEY=твой_публичный_адрес
PRIVATE_KEY=твой_приватный_ключ
```

<img width="300" height="142" alt="image" src="https://github.com/user-attachments/assets/135b9158-2c9a-4365-a808-af8acbce8ad7" />


3. Сохрани файл. Ctrl + S

---

## Шаг 5. Запускаем кошелёк

В терминале выполни:
<img width="1042" height="552" alt="image" src="https://github.com/user-attachments/assets/0fd0417a-0eed-4865-b0a9-bdfe844eae86" />


```bash
python wallet_cli.py
```

Если появилась ошибка — скопируй её текст и обратись за помощью к встроенному ИИ-агенту в Codespace, он поможет разобраться.

---

## Шаг 6. Работаем с меню

После запуска появится меню:
<img width="677" height="230" alt="image" src="https://github.com/user-attachments/assets/a5ef36e6-729a-4691-9215-1a3410a8bd4d" />


```
====================
 SOLANA WALLET CLI
====================
1. Show balance
2. Send SOL (demo)
3. Transaction history
4. Exit
```

Выбирай нужный пункт, вводя цифру:

| Пункт | Что делает |
|---|---|
| **1** | Показать баланс кошелька в SOL |
| **2** | Отправить SOL на другой адрес (нужно будет ввести адрес получателя и сумму) |
| **3** | Показать историю последних транзакций |
| **4** | Выйти из программы |

---

## Структура проекта

| Файл | Описание |
|---|---|
| `main.py` | Создаёт новый кошелёк или загружает существующий из `wallet.json` |
| `wallet_cli.py` | Главное меню: баланс, отправка SOL, история транзакций |
| `balance.py` | Отдельный скрипт для быстрой проверки баланса |
| `requirements.txt` | Список зависимостей Python |
| `command.txt` | Список команд для установки и запуска |
| `check-key.txt` | Ссылка на [Solscan](https://solscan.io) для проверки адреса/транзакций вручную |

---

## Проверка кошелька

Проверить баланс, адрес и транзакции можно также вручную на [Solscan](https://solscan.io), просто вставив свой публичный адрес в поиск.

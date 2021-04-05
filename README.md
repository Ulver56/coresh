# Coresh

.jobs:
run_tests:
runs-on: "ubuntu-latest"
steps:

      # Чекаутим код
      - name: Check Out Repo
      - uses: actions/checkout@master

      # Устанавливаем python нужной версии
      - uses: actions/setup-python@v1
        with:
          python-version: "3.8"
          architecture: "x64"

      # Устанавливаем зависимости
      - name: Install requirements
        run: pip install -r requirements.txt

      # Прогоняем тесты
      - name: Run tests
        run: echo 1

      # Логинимся в докере
      - name: Login to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_LOGIN }}
          password: ${{ secrets.DOCKER_ACCESS_TOKEN }}


# commands in project

Этот README.md актуально только если работать с папкой base_site как с отдельным проектом

## только если с нуля самому от А до Я

```poetry new src```

```poetry shell```

```poetry add grpcio```

```poetry add grpcio-tools```

- создать папку src/rpc

```bash
mkdir rpc
```

- создать файл прото:

```bash
# example -> touch your_name.proto
touch AuthService.proto
```

```bash
cd dir_to_proto_file/
ls
# example.proto

- наполнить данными

```

- скопилить .proto

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. AuthService.proto
```

## Если уже работать с данными кодом, то

- инициализировать проект

```bash
poetry install
```

- активировать окружение

```bash
poetry shell
```

запустить:

```bash
make start
# or
python src/main.py 
```

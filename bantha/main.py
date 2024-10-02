import json
from genson import SchemaBuilder
import typer


app = typer.Typer()


@app.command()
def generate_schema(source_path: str, destination_path: str):
    with open(source_path, "r") as fp:
        source = fp.read()

    builder = SchemaBuilder()
    builder.add_object(source)

    schema = builder.to_schema()

    with open(destination_path, "w") as fp:
        json.dump(schema, fp, indent=2)


if __name__ == "__main__":
    app()

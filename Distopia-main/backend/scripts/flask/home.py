def init():
    html = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Esteganografia API</title>
            </head>
            <h1> Esteganografia API </h1>
                <form action="/upload" method="post" enctype="multipart/form-data">
                    <input type="file" name="imagem"><br><br>
                    <label for="mensagem">Mensagem:</label><br>
                    <textarea name="mensagem" id="mensagem"></textarea><br><br>
                    <input type="submit" value="Enviar imagem e mensagem">
                </form>
                <br>
                <form action="/image" method="get">
                    <input type="submit" value="Veja imagem">
                </form>
                <br>
                <form action="/reveal" method="post" enctype="multipart/form-data">
                    <input type="file" name="imagem"><br><br>
                    <input type="submit" value="Revelar mensagem">
                </form>
            </body>
        </html>
    """
    return html

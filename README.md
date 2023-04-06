<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css" integrity="sha512-1sCRPdkRXhBV2PBLUdRb4tMg1w2YPf37qatUFeS7zlBy7jJI8Lf4VHwWfZZfpXtYSLy85pkm9GaYVYMfw5BC1A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    {% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
    <title>Lab - 03</title>
</head>

<body>
    <!-- HEADER -->
    <div class="container-header">
        <header>
            <div class="logo">
                <a href="#">QJ Developer</a>
            </div>
            <nav id="nav">
                <ul>
                    <li><a href="/" onclick="seleccionar()"><i class="fa-solid fa-house"></i> INICIO</a></li>
                    <li><a href="/encuesta" onclick="seleccionar()"><i class="fa-solid fa-question"></i> PREGUNTAS</a></li>
                    <li><a href="/votos" onclick="seleccionar()"><i class="fa-solid fa-check-to-slot"></i> VOTOS</a></li>
                </ul>
            </nav>
            <div class="nav-responsive" onclick="mostrarOcultarMenu()">
                <i class="fa-solid fa-bars"></i>
            </div>
        </header>
    </div>

    <!-- ------MAIN---------->
    <section id="home" class="home">
        <div class="content-banner">
            {% block main %}
            <div class="container-img">
                <img src="{% static 'img/foto.jpg' %}" alt="">
            </div>
            <h1>FREDDY QUEA</h1>
            <h2>DESARROLLO DE APLICACIONES EMPRESARIALES</h2>
            <div class="lab">
                <h2>LABORATORIO - 03</h2>
            </div>
            {% endblock %}
        </div>
    </section>

    <!-- footer -->
    <footer>
        <a href="#home" class="arriba">
            <i class="fa-solid fa-angles-up"></i>
        </a>
        <div class="redes">
            <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="#"><i class="fa-brands fa-instagram"></i></a>
            <a href="#"><i class="fa-brands fa-github"></i></a>
            <a href="#"><i class="fa-brands fa-discord"></i></a>
        </div>
    </footer>

    <script src="{% static 'js/script.js' %}"></script>
</body>

</html>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oxygen">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Ubuntu">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    {% block head %} {% endblock %}
</head>

<body style="background: linear-gradient(rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.5)), url(&quot;assets/img/99a9d89b174548f4c6be1462c06ae6a9.jpg&quot;) center / cover;">
    <nav class="navbar navbar-light navbar-expand-md" style="background: #121212;font-family: Roboto, sans-serif;border-bottom-color: rgb(255,255,255);padding-right: 10%;padding-left: 10%;">
        <div class="container-fluid"><a class="navbar-brand" href="#" style="color: rgb(225,225,225);font-family: Ubuntu, sans-serif;">portfol.io</a>
            <div class="collapse navbar-collapse" id="navcol-1">
                <ul class="navbar-nav ms-auto">

                    {% if session['userid'] %}
                        <li class="nav-item" style="color: rgb(255,255,255);">
                            <a class="nav-link active" href="/dashboard/" style="color: rgb(225,225,225);letter-spacing: 1.5px;">dashboard</a>
                        </li>

                        <li class="nav-item font-monospace">
                            <a class="nav-link" href="/profile/" style="color: rgb(225,225,225);font-family: Roboto, sans-serif;letter-spacing: 1.5px;">profile</a>
                        </li>

                        <li class="nav-item" style="color: rgb(255,255,255);">
                            <a class="nav-link" href="/logout/" style="color: rgba(225,10,10,0.5);letter-spacing: 1.5px;">logout</a>
                        </li>
                    {% endif %}

                    {% if not session['userid'] %}
                        <li class="nav-item" style="color: rgb(255,255,255);">
                            <a class="nav-link" href="/login/" style="color: rgba(225,225,225,0.5);letter-spacing: 1.5px;">login / sign-up</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    {% block body %} {% endblock %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
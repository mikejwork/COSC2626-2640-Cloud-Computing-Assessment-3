{% extends 'template.php' %}


{% block head %}

<title>portfol.io - home</title>

{% endblock %}



{% block body %}

<section style="padding: 15%;font-family: Ubuntu, sans-serif;border-top: 1px inset rgba(255,255,255,0.07);">
    <div class="container" style="color: rgb(255,255,255);padding: 2%;background: rgba(18,18,18,0);border-radius: 15px;font-family: Ubuntu, sans-serif;">
        <h1 style="font-weight: normal;font-style: normal;font-family: Ubuntu, sans-serif;">Welcome to your Portfol.io</h1>
        <p style="font-family: Ubuntu, sans-serif;">Manage and track your assets with ease, using cloud storage and market APIs to track where your portfolio is headed.</p>
        <div>
            <form action="/login/" class="d-xl-flex align-items-xl-center">
                <input class="form-control" type="text" style="width: 35%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;" placeholder="Email address">
                <button class="btn btn-primary" type="button" style="background: rgba(36,121,221,0.71);border-width: 0px;font-family: Ubuntu, sans-serif;border-top-left-radius: 0px;border-bottom-left-radius: 0px;">Get Started<i class="fa fa-long-arrow-right" style="margin-left: 10px;"></i></button>
            </form>
        </div>
    </div>
</section>

{% endblock %}
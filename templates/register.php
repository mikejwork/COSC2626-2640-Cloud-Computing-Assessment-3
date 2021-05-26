{% extends 'template.php' %}


{% block head %}

<title>portfol.io - register</title>

{% endblock %}



{% block body %}

<section style="padding: 15%;font-family: Ubuntu, sans-serif;border-top: 1px inset rgba(255,255,255,0.07);">
    <div class="container" style="color: rgb(255,255,255);padding: 2%;background: rgba(18,18,18,0);border-radius: 15px;font-family: Roboto, sans-serif;">
        <h1 style="font-weight: normal;font-style: normal;font-family: Ubuntu, sans-serif;">sign-up</h1>
        <p style="font-family: Ubuntu, sans-serif;">Enter your details below to create an account.</p>

        <form style="margin-bottom: 5px;">
            <input id="email_field" name="email_field" class="form-control" type="email" style="width: 40%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;margin-bottom: 10px;" placeholder="Email address">
            <input id="fullname_field" name="fullname_field" class="form-control" type="text" style="width: 40%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;margin-bottom: 10px;" placeholder="Full name">
            <input id="username_field" name="username_field" class="form-control" type="text" style="width: 40%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;margin-bottom: 10px;" placeholder="Username">
            <input id="phonenumber_field" name="phonenumber_field" class="form-control" type="text" style="width: 40%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;margin-bottom: 10px;" placeholder="Phone number">
            <input id="password_field" name="password_field" class="form-control" type="password" style="width: 40%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;margin-bottom: 10px;" placeholder="Password">
            <button class="btn btn-primary" type="submit" style="background: rgba(36,121,221,0.71);border-width: 0px;font-family: Ubuntu, sans-serif;border-top-left-radius: 0px;border-bottom-left-radius: 0px;width: 40%;">
                Register<i class="fa fa-long-arrow-right" style="margin-left: 10px;"></i>
            </button>
        </form>
        
        <a href="/login/" style="color: rgb(255,255,255);font-family: Ubuntu, sans-serif;text-decoration: none;">Already have an account?</a>
    </div>
</section>

{% endblock %}
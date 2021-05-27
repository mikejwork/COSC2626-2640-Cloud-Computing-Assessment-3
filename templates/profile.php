{% extends 'template.php' %}


{% block head %}

<title>portfol.io - profile</title>

{% endblock %}



{% block body %}

<section style="padding: 15%;font-family: Ubuntu, sans-serif;border-top: 1px inset rgba(255,255,255,0.07); padding-top:0px;">
    <div class="container" style="color: rgb(255,255,255);padding: 2%;background: rgba(18,18,18,0);border-radius: 15px;font-family: Ubuntu, sans-serif;">
        <div style="margin-bottom: 5%;">
            <h1 style="font-weight: normal;font-style: normal;font-family: Ubuntu, sans-serif;">My Profile</h1>
            <p style="font-family: Ubuntu, sans-serif;margin-bottom: 5px;margin-left: 25px;border-bottom-color: rgb(255,255,255);"><strong>Username</strong>:  {{user.username}}</p>
            <p style="font-family: Ubuntu, sans-serif;margin-bottom: 5px;margin-left: 25px;"><strong>Email Address</strong>:  {{user.email}}</p>
            <p style="font-family: Ubuntu, sans-serif;margin-bottom: 5px;margin-left: 25px;"><strong>Phone Number</strong>:  {{user.phonenumber}}</p>
        </div>
        <div>
            <h1 style="font-weight: normal;font-style: normal;font-family: Ubuntu, sans-serif;">Change Password</h1>

            <form action="/changepassword/" method="POST" style="margin-bottom: 5px;">
                <input id="current_password" name="current_password" class="form-control" type="password" style="width: 40%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;margin-bottom: 10px;" placeholder="Current password">
                <input id="desired_password" name="desired_password" class="form-control" type="password" style="width: 40%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;margin-bottom: 10px;" placeholder="Desired password">
                <button class="btn btn-primary" type="submit" style="background: rgba(36,121,221,0.71);border-width: 0px;font-family: Ubuntu, sans-serif;border-top-left-radius: 0px;border-bottom-left-radius: 0px;width: 40%;">Change<i class="fa fa-long-arrow-right" style="margin-left: 10px;"></i></button>
            </form>

        </div>
    </div>
</section>

{% endblock %}
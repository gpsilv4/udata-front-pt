# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from udata_front import theme
from udata import i18n
from udata.i18n import I18nBlueprint
from flask import (
    request, 
    current_app, 
)
import redis

from urllib.parse import urlparse
from flask_wtf import FlaskForm, recaptcha
from wtforms.fields import EmailField
from udata.forms import fields, validators
from flask_mail import Message
from flask_security.utils import do_flash

from udata.models import Organization


class ContactForm(FlaskForm):
    name = fields.StringField("Name", [validators.DataRequired()])
    email = EmailField("Email", [validators.DataRequired(), validators.Email()])
    subject = fields.StringField("Subject", [validators.DataRequired()])
    message = fields.TextAreaField("Message", [validators.DataRequired()])
    recaptcha = recaptcha.RecaptchaField()

def get_redis_connection():
    parsed_url = urlparse(current_app.config['CELERY_BROKER_URL'])
    db = parsed_url.path[1:] if parsed_url.path else 0
    return redis.StrictRedis(host=parsed_url.hostname, port=parsed_url.port,
                             db=db)

blueprint = I18nBlueprint('gouvfr_faq', __name__,
                          template_folder='../theme/templates/custom',
                          static_folder='../theme/static')

#Contact Form page
@blueprint.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            for field, errors in form.errors.items():
                for error in errors:
                    do_flash(i18n.gettext(error),'danger')
        else:
            msg = Message(form.subject.data, sender=current_app.config.get('MAIL_DEFAULT_SENDER'), recipients=[current_app.config.get('MAIL_DEFAULT_RECEIVER')])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            try:
                mail = current_app.extensions.get('mail')
                mail.send(msg)
            except Exception as e:
                do_flash("Server Error : " + str(e), 'danger')
            else:
                do_flash(i18n.gettext(u"Thank you for your message. We'll get back to you shortly."), 'success')
    return theme.render('custom/contact.html', form=form)

#Add docapi
@blueprint.route('/docapi/')
def docapi():
    organizations = Organization.objects.all()
    return theme.render('custom/api.html', organizations=organizations)
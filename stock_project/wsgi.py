
import sys
import os
from pathlib import Path

# أضف المسار الكامل لمجلد المشروع
project_path = '/home/ObadaEz/stock_project/'
if project_path not in sys.path:
    sys.path.append(project_path)

# إعداد Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'stock_project.settings'

# تحميل تطبيق WSGI الخاص بـ Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from django.shortcuts import render
import datetime

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from fff_app.models import Flight, Order


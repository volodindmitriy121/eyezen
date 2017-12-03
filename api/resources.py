from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
import test_api.models as ta
from tastypie import fields

class UserResource(ModelResource):

    class Meta:
        queryset = ta.User.objects.all()
        resource_name = 'user'
        authorization = Authorization()

class SensorResource(ModelResource):

    resqueteam = fields.ForeignKey('ResqueTeamResource', 'resqueteam')

    class Meta:
        queryset = ta.Sensor.objects.all()
        resource_name = 'sensor'
        authorization = Authorization()


class OperatorResource(ModelResource):
    class Meta:
        queryset = ta.Operator.objects.all()
        resource_name = 'operator'
        authorization = Authorization()

class ResqueTeamResource(ModelResource):
    class Meta:
        queryset = ta.ResqueTeam.objects.all()
        resource_name = 'resqueteam'
        authorization = Authorization()

class TerritoryResource(ModelResource):

    sensor = fields.ForeignKey(SensorResource, 'sensor')

    class Meta:
        queryset = ta.Territory.objects.all()
        resource_name = 'territory'
        authorization = Authorization()


class User_operatorsResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user')
    operators = fields.ForeignKey(OperatorResource, 'operator')

    class Meta:
        queryset = ta.User_operators.objects.all()
        resource_name = 'user_operators'
        authorization = Authorization()



class Oper_on_terrResource(ModelResource):

    territory = fields.ForeignKey(TerritoryResource, 'territory')
    operators = fields.ForeignKey(OperatorResource, 'operator')

    class Meta:
        queryset = ta.Oper_on_terr.objects.all()
        resource_name = 'oper_on_terr'
        authorization = Authorization()
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Test(APIView):
    @staticmethod
    def post(request):
        id = request.data.get('id')

        if not (id and id.isdigit()):
            data = dict(error="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        id = int(id)

        names = {
            1: 'Артём',
            2: 'Антон',
            3: 'Артём',
            4: 'Паша',
            5: 'Ваня',
        }
        data = dict(status="Success!", name=names.get(id))
        return Response(data=data, status=status.HTTP_200_OK)

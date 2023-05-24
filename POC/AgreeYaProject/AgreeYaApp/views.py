import csv
import json
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import scrubadub


# Create your views here.

def index(request):
    text = "My cat can be contacted on example@example.com, or 1800 555-5555"
    # scrb = scrubadub.clean(text)
    if request.method == "POST":
        # import sys
        # # sys.path.append("C:\Program Files\JetBrains\PyCharm 2017.2.3\debug-eggs")
        # sys.path.append("D:\pycharm-debug")
        # import pydevd
        # pydevd.settrace('localhost', port=9086, stdoutToServer=True, stderrToServer=True)
        import pandas as pd
        filename = request.FILES['data_file']
        print(">>.", filename)
        data_read = pd.read_csv(filename, encoding='utf8')
        # name = data_read["Name"]
        # address = data_read["Address"]
        # phone = data_read["Phone"]
        # email = data_read["Email"]
        column_names = list(data_read.columns)

        # check_file_exist = Record_data.objects.filter(Filepath=filename).exists()
        # print("ddddddddddd>>>",check_file_exist)
        # if check_file_exist == False:
        #     data_record = Record_data(
        #         Name=name,
        #         Address=address,
        #         Phone=phone,
        #         Email=email,
        #         Filepath=filename,
        #     )
        #     # data_record.save()
        # mydata = Record_data.objects.all()

        # data_lst=[x for x in mydata]
        # print("DAtata11111111",mydata)
        # print("DAtata",data_lst)
        # import pdb
        # pdb.set_trace()
        return render(request, "index.html", {"msg1": "File upload Successfully", "column": column_names})
    return render(request, "index.html")


def upload_crub_data(request):
    import time
    # import sys
    # sys.path.append("D:\pycharm-debug")
    # import pydevd
    # pydevd.settrace('localhost', port=9086, stdoutToServer=True, stderrToServer=True)
    if request.method == 'POST' and request.FILES['upload_csv_file']:
        csv_file = request.FILES['upload_csv_file']
        if not csv_file.name.endswith('.csv'):
            return JsonResponse({'error': 'File is not a CSV'})

        # Save the uploaded file to a specified location on the server
        actual_file= str(time.time())+'_'+csv_file.name
        with open('./media/'+actual_file, 'wb+') as destination:
        # with open('./media/scrub/csv_file.csv', 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)
        return JsonResponse({'success': True, 'filename':actual_file})
    else:
        return JsonResponse({'error': 'POST request required'})


def get_csv_headers(request):
    filename =request.GET.get('filename')
    if request.is_ajax() and request.method == 'GET':
        with open('./media/'+filename) as csv_file:
            # reading the csv file using DictReader
            csv_reader = csv.DictReader(csv_file)
            dict_from_csv = dict(list(csv_reader)[0])
            columns = list(dict_from_csv.keys())

        return JsonResponse({'success': True, 'data': columns})
    else:
        return JsonResponse({'success': False, 'error': 'Failed to fetch data from API'}, status=500)


def scrub_headers_data(request):
    import sys
    sys.path.append("D:\pycharm-debug")
    import pydevd
    pydevd.settrace('localhost', port=9086, stdoutToServer=True, stderrToServer=True)
    headers = request.GET.get('headers')
    headers = json.loads(headers)
    import time
    filename =request.GET.get('filename')
    if request.method == 'GET':
        file = './media/'+filename
        df = pd.read_csv(file)
        # scrub = lambda x: 'Srubbed-' + str(x)
        # s=df.set_index('Email',inplace=False)
        # scrub = lambda x: scrubadub.clean(x.decode('utf-8'), replace_with='identifier')
        scrub = lambda x: scrubadub.clean(str(x).encode().decode("unicode_escape").encode('raw_unicode_escape').decode(), replace_with='identifier')
        # data['name'] = data['name'].apply(
        #     lambda x: x[2:-1].encode().decode("unicode_escape").encode('raw_unicode_escape').decode()
        # )

        for h in headers:
            # s[h] = s[h].apply(scrub)
            df[h] = df[h].apply(scrub)
            print(df[h],'222222222222',type(str(df[h])))
            # df[h] = str(df[h]).replace(str(df[h].apply(scrub)), "John")
            # df[h]= df[h].replace(df[h].append(scrub),"John")
        write_file = './media/scrub/'+filename
        df.to_csv(write_file, encoding='utf-8', index=False)
        return JsonResponse({'success': True, 'data': headers,'file_names':write_file})
    else:
        return JsonResponse({'success': False, 'error': 'Failed to fetch data from API'}, status=500)

def download_file(request):
    filename =request.GET.get('filename')
    import time
    import sys
    # sys.path.append("C:\Program Files\JetBrains\PyCharm 2017.2.3\debug-eggs")
    # sys.path.append("D:\pycharm-debug")
    # import pydevd
    # pydevd.settrace('localhost', port=9086, stdoutToServer=True, stderrToServer=True)
    # # file_path = './media/scrub/scrubbed_csv_file.csv'
    file_path = './media/scrub/'+filename
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename="file.pdf"'
        return response

    return JsonResponse({'success': True})
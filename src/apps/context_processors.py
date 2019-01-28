from apps import model_choices as mch

def global_context(request):
    return {'mch': mch}
# like a variable, that I can use in all html files in context + context manualy from vievs.
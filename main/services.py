from main.models import ToDo

def get_todo_list():
    """Getting all the entries from the ToDo model"""
    queryset = ToDo.objects.all()
    return queryset

def create_todo(title, description):
    """Create a new entry in the ToDo model"""
    todo = ToDo()
    todo.title = title
    todo.description = description
    todo.save()

def get_todo_via_pk(pk):
    """Get an entry via pk"""
    obj = ToDo.objects.get(id=pk)
    return obj

def delete_todo(pk):
    """Delete an entry via pk"""
    obj = ToDo.objects.get(id=pk)
    obj.delete()
    return obj

def edit_todo(title, description, pk):
    """Create a new entry in the ToDo model"""
    obj = ToDo.objects.get(pk=pk)
    obj.title = title
    obj.description = description
    obj.save()
    return obj
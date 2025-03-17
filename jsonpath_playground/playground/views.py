# playground/views.py
from django.shortcuts import render
import json
from jsonpath_ng import parse

def playground_view(request):
    result = None
    error = None
    json_data = ""
    json_path = ""
    
    if request.method == "POST":
        # Retrieve form inputs
        json_data = request.POST.get("json_data", "")
        json_path = request.POST.get("json_path", "")
        
        try:
            data = json.loads(json_data)
            
            jsonpath_expr = parse(json_path)
            
            result = [match.value for match in jsonpath_expr.find(data)]
        except Exception as e:
            error = f"Error: {str(e)}"
    
    # Render the template with context data.
    return render(request, "playground/playground.html", {
        "result": result,
        "error": error,
        "json_data": json_data,
        "json_path": json_path
    })

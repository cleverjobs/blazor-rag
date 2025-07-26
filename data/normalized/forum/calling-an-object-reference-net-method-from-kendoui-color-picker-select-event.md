# Calling an object reference .NET method from KendoUI Color Picker select event

## Question

**Chr** asked on 09 Jul 2020

Hey all, I'm working on a wrapper for the KendoUI color picker to allow users more control over the colors of how their data is being represented. So the overall flow will be, given a dynamic list of data, create a color picker for each one, passing an object reference for that specific item. Then, upon a color being picked, call a function on that object to update it's color property with the selection. My problem being that I can't figure out how to get the object reference into the color changed event. I thought using JS protoyped functions would work (because I need each color picker to have it's own scope so it knows which object's function to call) but 'this' inside of ColorPickerWidget is scoped to the window instead of to ColorPickerWidget. Any suggestions would be appreciated! JS functions: function ColorPickerWidget(bindTo, objRef) { var objectRef=objRef; this.create(bindTo); }; ColorPickerWidget.prototype.create=function(bindTo) { $(bindto).kendoColorPicker({ value: "#ffffff", buttons: false, select: this.selectColor }); } ColorPickerWidget.prototype.selectColor=function(e) { this.objectRef.invokeMethodAsync("ChangeColor", e.value); } .NET Functions: protected async override Task OnInitializedAsync() { await JsRuntime.InvokeVoidAsync(identifier: "ColorPickerWidget", elRef, DotNetObjectReference.Create(this)); } [JSInvokable] public void ChangeColor(string color) { Color=color; ColorChanged.InvokeAsync(color); }

## Answer

**Marin Bratanov** answered on 10 Jul 2020

Hi Chris, You may find this thread helpful on keeping a reference to the object you want: [https://stackoverflow.com/questions/20279484/how-to-access-the-correct-this-inside-a-callback.](https://stackoverflow.com/questions/20279484/how-to-access-the-correct-this-inside-a-callback.) You may also consider instantiating an object for each picker in the JS side - this will let you create it on initialization and use a field in it to store the respective .NET object reference that you will later use to call the Blazor code. This will also let you clean up the appropriate instance in the Dispose method of the razor component. Keeping all fields in the same prototype level will also facilitate accessing them. Regards, Marin Bratanov

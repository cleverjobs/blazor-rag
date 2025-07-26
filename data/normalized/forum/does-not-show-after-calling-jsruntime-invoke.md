# Does not show after calling JSRuntime.Invoke

## Question

**Jon** asked on 11 May 2020

Hi.. I have the following code. After JSRuntime is called the AnimationContainer does not show. I get a screen flicker. Any idea how I can show the Animation Container after opening (downloading a file) thanks again! await JSRuntime.InvokeAsync<object>("open", URI, "_blank"); await AnimationContainer.ShowAsync(); StateHasChanged(); await Task.Delay(5000); await AnimationContainer.HideAsync(); StateHasChanged();

## Answer

**Marin Bratanov** answered on 11 May 2020

Hello Jonathan, The provided code snippet throws an error in the window.open call, which breaks the entire app. I am attaching a short video that demonstrates this. I strongly advise that you monitor the browser console to ensure there are no errors. Blazor cannot take circular JS object references, and the window object returned from window.open has a circular reference - its .parent field points to the current window instance. A workaround for that can be defining you own function that does not create a circular reference because it will never serialize a return type back to Blazor. For your convenience, I am attaching a sample of this. Regards, Marin Bratanov

### Response

**Jonathan** answered on 11 May 2020

Awesome!.. thx again

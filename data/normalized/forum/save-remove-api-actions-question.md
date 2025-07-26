# Save & Remove api Actions question

## Question

**BobBob** asked on 11 Sep 2020

Both of these events take a collections of items (IEnumerable<IFormFile> for Save and string[] for Remove). My question is why?? It appears that these methods are called for each file uploaded (or removed). It appears it is this way regardless of whether I auto upload or not? Why can't I just send the method 1 item instead of a collection of items???

## Answer

**Marin Bratanov** answered on 11 Sep 2020

Hello Bob, This is just an example for an ASP.NET Core controller action so it can read the multipart form (theoretically, there could be many files in it). You are free to use any suitable endpoint that matches your needs, technology (it does not even have to be .NET) and can read a file from the POST query. I made for you a sample that uses a single file upload and the controller action takes a single file and you can find it attached at the end of this post. You can see how the argument name of the action matches the SaveField of the component and how multiple file uploads are disabled. Note that with automatic uploads disabled, a user could still upload several files at once even if multiple file selection is disabled. Regards, Marin Bratanov

### Response

**Bob** answered on 11 Sep 2020

Thanks, I will check it out. I guess my confusion is I am allowing multiple files to be uploaded in my upload control. I though that it would send all the files into the method (as an Ienumerable like the action takes), but it doesn't. It literally calls the action for every file that has been selected to be uploaded? Is there any way to make it take the complete list of files selected in one call rather than multiple calls to the api??

### Response

**Marin Bratanov** answered on 11 Sep 2020

Hello Bob, Each file is sent on its own. You don't have to use an IEnumerable collection, as shown in my previous post. Regards, Marin Bratanov

### Response

**Bob** answered on 11 Sep 2020

I understand and will adjust my code. If each file is sent on it's own then why would anyone ever use an IEnumerable like you have in your demo examples? Doesn't make sense if the method will ONLY ever receive one file at a time.

### Response

**Marin Bratanov** answered on 11 Sep 2020

Hi Bob, The endpoint does not have to be specifically created for this widget, it may be existing already and it may accommodate various scenarios. Regards, Marin Bratanov

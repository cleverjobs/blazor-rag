# FIlemanager Upload dialog events

## Question

**Kee** asked on 09 Jun 2022

Hello, I think I'm missing something in the (sparse) documentation of the Upload part of the Filemanager component, specifically this page: [https://docs.telerik.com/blazor-ui/components/filemanager/upload](https://docs.telerik.com/blazor-ui/components/filemanager/upload) The sample provided on this page places uploaded files in the FlatFileEntry list before clicking on the button OK or Cancel on the Upload dialog. I don't want that, I want to update the FlatFileEntry list after clicking OK or doing nothing (or discarding the uploaded file still at its temporary location where the api did put it) after clicking Cancel. Which events are fired after clicking on these buttons? Does anyone have some sample code that is a bit more verbose than the almost identical sample that is pasted on every documentation page? Kind regards, Kees Alderliesten

### Response

**Hristian Stefanov** commented on 14 Jun 2022

Hi Kees, Thank you for providing feedback on the documentation. There is always space for improvement. Most of the examples in the documentation articles are with hard-coded data and show partly configurations. That is the case because we are trying to keep the articles readable and not too long. The idea is to show the developers that there is a functionality that they can configure as desired. The case is different for the demos. The demos are made to show more complex (real-world scenario) configurations. Here is the FileManager demo to test more in-depth the functionalities: Blazor FileManager - Overview. Additionally, here are details about the events FileManager exposes: FileManager Events. I hope you find the above information helpful. Let me know if I can help with anything else, or if there is a specific place to improve, and at the same time keep the examples short/basic.

### Response

**Kees** commented on 15 Jun 2022

Hi Hristan, Those documentation en demo pages you link to are the reason I asked my question ;-) Because I'm missing something. If you run the demo you will notice that after uploading a file (take one with a name starting with a Z, otherwise the change is less visible because it may be behind the popup) the file is already placed in the folder (and thus the underlying filesystem or wherever the files are stored) before you click OK. So, if you realize you uploaded the wrong file and then click the Cancel button (or the small x beside the filename) the file is removed from the folder (and filesystem), but between these moments the file was visible to other users. What I expected was that the files are kept at the location where the upload api stores them and are placed in the folder (and filesystem) after clicking OK (and removed from the temporary storage after clicking Cancel) I tried to build it that way but couldn't find an event that is fired after clicking OK. The OK button now just closes the popup. Or am I indeed missing something?

### Response

**Hristian Stefanov** commented on 20 Jun 2022

Hi Kees, You have good observations of the component's current behavior. I confirm the provided expectations make sense. It turns out we have planned a revision of the whole FileManager design. One of the points in the revision is about the uploading functionality. I will be sharing your feedback on every discussion we have with the team. Additionally, after the revision, we may also expose the upload dialog. That will make uploading on dialog button click possible. Thank you once again.

### Response

**Kees** commented on 20 Jun 2022

Hi Hristan, Thank you and good to hear! For now, I will implement it the same way as the demo works and then I will eagerly await the revised Filemanager ;-) Is there a feature request or something which I can follow or should I check the roadmaps and release notes? Kind regards, Kees Alderliesten

### Response

**Hristian Stefanov** commented on 23 Jun 2022

Hi Kees, After the revision, we will notify in public. Additionally, new ideas for feature requests may appear in the Public Feedback Portal. The best way to track the process is to keep an eye on the release notes and the

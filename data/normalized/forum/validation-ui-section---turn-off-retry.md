# Validation UI section - turn off retry

## Question

**Bit** asked on 12 Oct 2020

Is there a way to turn off the "retry" element after a file has been selected and it has errored?

## Answer

**Marin Bratanov** answered on 13 Oct 2020

Hello, If the reason you're asking is because retrying does not fire OnUpload again, you can Follow a fix for that here. I've also added there a bit of CSS that you can use to hide the retry button. Regards, Marin Bratanov

### Response

**BitShift** answered on 14 Oct 2020

Well, in my situation I have defined filetype restictions, which seems to fire client-side validation but I also do server-side checks on the file before saving the file to its destination, and if those checks fail I return a BadRequestObjectResult and use an error handler. So maybe the best way to deal with this is to either do all the checks server-side, but when the error happens I am just showing an alert via a modal window component. How could I turn off / hide the file "history" that shows up after an upload?

### Response

**Marin Bratanov** answered on 14 Oct 2020

Hello, There are two feature requests for something similar to that - please check them and see which is the one you need so you can Vote for it and Follow it: removing all files in the current list: [https://feedback.telerik.com/blazor/1485661-clear-current-files-in-blazor-upload](https://feedback.telerik.com/blazor/1485661-clear-current-files-in-blazor-upload) being able to add files yourself to the list even without the user uploading them: [https://feedback.telerik.com/blazor/1485660-initial-files-in-blazor-upload](https://feedback.telerik.com/blazor/1485660-initial-files-in-blazor-upload) From what I understand, the file would never be able to be valid in your case, so re-uploading would not make sense and thus hiding the Retry button with CSS should work. It would, perhaps be nice if you could remove it and keep the list of successful ones, which would be possible after both features above are implemented. If this is not what you seek, could you provide some more details on what functionality you would want from the component? It is important to consider that the Retry button may be meaningful if some metadata on the file can change (which is something you collect through OnUpload), or there was a network issue. Regards, Marin Bratanov

### Response

**BitShift** answered on 15 Oct 2020

Hmm, yes I think either clearing this list after an upload (whether successful or not) would help, but also having the option to enable/disable this list completely I think would also help. In the UI, after an upload there is a <ul> element with class="k-upload-files k-reset" that I guess I could just set visibility=none? I think its this option that would better fit what I am trying to do

### Response

**Marin Bratanov** answered on 16 Oct 2020

Hello, You could use CSS to hide the list, there is no issue with that. You could wrap the upload in a <div> whose class you can set dynamically based on a flag you raise in OnSuccess or OnError, in order to cascade through it and hide the list conditionally, if you don't want to hide it all the time. Regards, Marin Bratanov

### Response

**BitShift** answered on 19 Oct 2020

Wouldnt want to hide the entire upload widget, just the file(s) history that shows after an upload. What css would I use to hide just the list? I believe its an <ul> element that is only added to the UI after the upload?

### Response

**Marin Bratanov** answered on 19 Oct 2020

Hi, The following blog post can help you inspect the HTML rendering and classes in order to devise the rule you need for the outcome you want: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools) Regards, Marin Bratanov

### Response

**BitShift** answered on 19 Oct 2020

I think I found another way, just place the Upload widget in a wrapping div that has a height not much more than the button and the file history wont be visible.

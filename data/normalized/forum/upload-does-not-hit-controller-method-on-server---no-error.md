# Upload does not hit controller method on server - no error

## Question

**Ren** asked on 02 Apr 2024

I have developed quite a large application with multiple file upload points in the UI to upload various files. All was working fine. Now one of the upload components stopped working. What I mean by this is that all the workflow methods (OnSelect, OnUpload) fire correctly but then, when it needs to call the server to process the upload, it just does nothing without returning an error or anything. The other upload components still work 100%. I have even copied the upload component tag from the razor page that is working and replaced the upload tag in the page that is not working and still it does not work. The difference is that on the one that is working it is on the page in a gridtoolbar while on the one that is not working the grid is on a tabstriptab on another page. The controller method is never hit and the browser console as well as the server logs do not indicate the upload post action being made. The solution is way too big to post here and I have already established that the upload can work. Does anyone have some pointers as to where and how to trace the probable cause of this behaviour?

## Answer

**Renier Pretorius** answered on 02 Apr 2024

Answering my own question for the sake of anyone coming across this. As I typed up the detail of my question a took a second look at the tabstrip implementation that I have done. I recently made a change to the page that allowed you to navigate to a specific tab on the page from another page, but the tab index defaulted to 0 (zero). So when the upload starts it seems to trigger a reset of the page which then jumped back to the first tab with the busy indicator active. I implemented the ActiveTabChanged method to remember the tab and now it all works again. If Upload in a tab or similar control, stay on it until upload complete

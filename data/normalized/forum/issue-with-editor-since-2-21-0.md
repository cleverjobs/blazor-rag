# Issue with Editor since 2.21.0

## Question

**Rog** asked on 25 Jan 2021

When we updated our packages to 2.21.0, it broke the Editor. I can no longer click inside the editor and type anything. When clicking the button to view the HTML it crashes. I reverted back to 2.20.0 where it works. No codes changes were made on our side. HTML: <TelerikEditor Class="mh-500" Height="@Height" @ref="editor" @bind-Value="Content" Tools="@EditorToolSets.All"></TelerikEditor> Properties: [Parameter] public string Content { get; set; } [Parameter] public string Height { get; set; }="auto"; private TelerikEditor editor { get; set; }

## Answer

**Marin Bratanov** answered on 25 Jan 2021

Hello Roger, I am attaching here a sample app and a short video where the editor seems to work fine for me in 2.21.0. Am I missing something? Can you reproduce the problem with this app so I can have a look? Regards, Marin Bratanov

### Response

**Roger** answered on 26 Jan 2021

Wow, thanks for the quick reply. I having been looking at this for awhile. I was able to reproduce the problem in the .sln that you provided (attached) but perhaps I am using something incorrectly. The pattern I was able to identify is if I use the TelerikUpload component to upload a file, it calls the success handler which changes the state that triggers the upload cmp to go away and triggers the editor to show. This will create the issue where the editor is not usable. If I don't trigger the upload cmp to go away in 2.21.0, it works. If I keep the code as it is, and downgrade to 2.20.0, it works. .SLN is below ADMIN EDIT: link removed because it shared the commercial packages publicly

### Response

**Marin Bratanov** answered on 26 Jan 2021

Hi Roger, This issue did reproduce for me only the first time when I used the files that came with your project (it still had the bin and obj folders). So, I went back to the project to look for issues, then I rebuilt it after adding a couple of console.writeline, and the issue went away. I am attaching a video of some of my tests so you can confirm if I am missing something, and also the app itself. The fact that it went away without meaningful changes to the code means to me that there was some sort of caching issue: perhaps your browser had cached the old js file clearing the browser cache could help, I show the easiest way to do that in the video (right click the reload button with the devtools open) perhaps the framework had cached the old file during the build and had not replaced it in the output, or perhaps the nuget packages on your machine are somehow corrupted. to avoid both, delete the bin and obj folders in all projects in your solution, then execute "dotnet nuget locals all --clear" in the CLI to clean up the local nuget cache, then open the project and rebuild it Could you give that a try and let me know how things go? On a side note, I deleted the link to your sample because it contains our commercial assemblies in the build output. In the future you can delete the bin and obj folders to both conserve space, and to ensure this does not happen (uploading our code publicly is a violation of our eula). Regards, Marin Bratanov

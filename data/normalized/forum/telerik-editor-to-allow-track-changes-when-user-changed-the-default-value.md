# Telerik Editor to allow track changes when user changed the default value

## Question

**Cla** asked on 10 Jan 2022

Hi, Is there any ways where we could implement a track changes feature? I do have a default word content available for the user, and the user will be able to change the content if required. The track change feature would allow reviewers to quickly zoom into the edited wording (i.e. highlighted in red) for them to review quickly. Is there any ways whereby I could implement this feature easily? Thank you!

## Answer

**Marin Bratanov** answered on 10 Jan 2022

Hello Claris, I made the following feature request on your behalf and I added some explanations on what I expect is most likely: [https://feedback.telerik.com/blazor/1548875-track-changes-functionality-in-the-editor.](https://feedback.telerik.com/blazor/1548875-track-changes-functionality-in-the-editor.) Your Vote is already in and since I made it on your behalf you are already subscribed for notifications. For the time being you can consider any of the publicly available HTML diff libraries (there are several on nuget.org, for example) to show changes to the user. Reconciling them, though, is not something that is easy to do at all, even if converting content to Word is relatively easy with our document processing libraries, diffing between HTML and Word does not carry over, only styling. Regards, Marin Bratanov

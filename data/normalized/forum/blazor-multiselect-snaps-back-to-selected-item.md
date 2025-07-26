# Blazor MultiSelect snaps back to selected item

## Question

**Eri** asked on 04 Oct 2024

I am trying to use a Telerik MultiSelect to allow the user to select multiple values with filtering, however with my initial implementation I am stumbling into an odd error where the first select item basically "prevents" scrolling. As you can see from above, I select the first item, but then no matter if I use my scroll wheel or the vertical scroller on the side, the component automatically snaps back to the selected item being in focus.. I am running the latest Telerik.UI.for.Blazor 6.2.0 and this project is a Blazor Maui app running .Net 8.0..

### Response

**Hristian Stefanov** commented on 08 Oct 2024

Hi Erik, Thank you for taking the time to record a video demonstrating the behavior. I attempted to reproduce the issue using a basic MultiSelect configuration, and everything appears to be working as expected on my end. It’s possible that I might be missing a key detail from your specific configuration that could help me replicate the problem. As the next step, could you share a small, runnable reproduction of the issue? For your convenience, you can send the code via the REPL platform. I look forward to your response and am eager to assist you further. Kind Regards, Hristian

### Response

**Erik** commented on 08 Oct 2024

Hristian, I have located the problem! I am multithreading this Maui app and had a background refresh running on the wrong thread which was causing the component to refresh with a StateHasChanged..

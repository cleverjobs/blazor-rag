# Issue with Min/Max Property

## Question

**Rog** asked on 10 Feb 2020

I am applying a min/max property to the DatePicker but it doesn't work as expected in the UI. In this example my Min is 7/24/18 and the current value that is bound to the property is 10/08/18. When I bring up the Calendar UI, I can see that the month of July is enabled and that June is disabled. But when I click on July it actually brings up October. Made a small video of it but can't upload it.

## Answer

**Marin Bratanov** answered on 10 Feb 2020

Hi Roger, In a support ticket you can attach archives, the forums only allow images. If you like, you could also upload the video to some cloud storage (like a google drive, etc.). In the meantime, could you check if this is what you are affected by: [https://feedback.telerik.com/blazor/1444160-min-and-max-don-t-limit-the-text-input-only-the-calendar?](https://feedback.telerik.com/blazor/1444160-min-and-max-don-t-limit-the-text-input-only-the-calendar?) Can you reproduce a problem with: the following snippet (the parameters have both getters and setters) <TelerikDatePicker @bind-Value="@date" Min="@min" Max="@max"></TelerikDatePicker>

@code{
DateTime date { get; set; }=DateTime.Now;
DateTime min { get; set; }=DateTime.Now.AddDays( -50 );
DateTime max { get; set; }=DateTime.Now.AddDays( 50 );
} our latest version (2.7.0 at the moment) Regards, Marin Bratanov

### Response

**Roger** answered on 10 Feb 2020

Looks like the issue that I am running into is different. Video [https://drive.google.com/open?id=1eYhQVDpS_hgkarEFtgx5Nq2gCR0rfbRc](https://drive.google.com/open?id=1eYhQVDpS_hgkarEFtgx5Nq2gCR0rfbRc)

### Response

**Marin Bratanov** answered on 10 Feb 2020

Hi Roger, Please modify my previous snippet to showcase this issue, as I am not sure how to reproduce it - both our demos and my previous snippet work fine for me, which indicates something specific must be happening in this case - either some setup on the component is wrong, or I am missing something. Regards, Marin Bratanov

# TextBox and NumericTextBox in mobile

## Question

**Gia** asked on 14 Sep 2022

Hi I want create a Blazor Server web app that we need use from mobile env. The only issue is that using TextBox and similar sometimes soft-keyboard overlap the editing area. Do you have any advise to optimize o minimize this issue ?

### Response

**Hristian Stefanov** commented on 16 Sep 2022

Hi Giampaolo, If it's convenient, can you please send a screenshot or video of the problem, so I can clearly see and understand it? What are the mobile phone and the browser used? I tried to reproduce the problem and opened our demo site on a mobile phone with a Chrome browser. I focused the TextBox so I can input text and the TextBox wasn't overlapping with the keyboard, because the browser automatically scrolls the input on the visible part of the screen. This was valid even when the TextBox was on the bottom of the screen at the time of the focusing. You can reproduce the described problem on the attached demo link above. I look forward to your reply. Kind regards, Hristian

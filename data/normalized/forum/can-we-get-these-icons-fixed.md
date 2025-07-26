# Can we get these icons fixed?

## Question

**Dan** asked on 14 Feb 2024

Noticed today that when opened in Figma, these "warning-circle" icons appear (as we suspected) that the top portion of the exclamation mark is not cut through the image. It should look like the "warning-triangle". Any update or info on this would be much appreciated. Thanks in advance!

## Answer

**Dimo** answered on 19 Feb 2024

Hi Daniel, Thanks for reporting this! I have notified my colleagues and awarded you Telerik points. Fortunately, the problem is only in the design system / Figma. The icons work in actual apps and you can use them immediately: [https://blazorrepl.telerik.com/GoYwbNPF360SXdpD57](https://blazorrepl.telerik.com/GoYwbNPF360SXdpD57) Regards, Dimo Progress Telerik

### Response

**Daniel** commented on 20 Feb 2024

Thanks for the reply, I am not seeing that in my experience. I see now that on your site it shows correctly: However when I try it myself in my code: <TelerikSvgIcon Icon="@SvgIcon.WarningCircle" Size="@ThemeConstants.SvgIcon.Size.Medium" /> This is the result:

### Response

**Dimo** commented on 20 Feb 2024

Aha, so it turns out you need components version 5.1.0 or later.

### Response

**Daniel** commented on 20 Feb 2024

I was on 4.6.0 so I just updated to 5.1.0 however I am still seeing the same thing.

### Response

**Dimo** commented on 20 Feb 2024

Are you sure? This is with 5.1.0: [https://blazorrepl.telerik.com/GyuQmOPU10GCJeKF30](https://blazorrepl.telerik.com/GyuQmOPU10GCJeKF30)

### Response

**Daniel** commented on 20 Feb 2024

Positive: Your example: SVG Path " M256 480c123.7 0 224-100.3 224-224S379.7 32 256 32 32 132.3 32 256s100.3 224 224 224m-32-352h64v160h-64zm0 256v-64h64v64z " My Project SVG Path " M256 480c123.7 0 224-100.3 224-224S379.7 32 256 32 32 132.3 32 256s100.3 224 224 224Zm-32-352v160h64V128h-64Zm0 256v-64h64v64h-64Z " If I paste yours into my browser it works.

### Response

**Daniel** commented on 20 Feb 2024

Aww we are on 5.0.1 not 5.1.0..... this says its the most up to date version:

### Response

**Dimo** commented on 21 Feb 2024

Please purchase a new license or ask the license holder at your company to assign you one, so that you have access to the latest version.

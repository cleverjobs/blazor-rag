# ImageUrl change for v4.0

## Question

**cma** asked on 20 Jan 2023

I've made the appropriate changes in all cases but this one -- What would be the correct change here? <TelerikButton Class="mr-1" ButtonType="@ButtonType.Button" ImageUrl=@GetImageUrl(@name) OnClick="@(()=>AttachmentOnClickHandler(name))"> @name </TelerikButton>

### Response

**cmarsh** commented on 20 Jan 2023

Thank you - we will give this a try. Unfortunately, v4.0 has killed lots of data calls and we can't figure out why:(

### Response

**Nadezhda Tacheva** commented on 25 Jan 2023

Hi Chris, I am sorry to hear that. I see my colleagues are working on this matter in another ticket of yours. Hopefully, the issue is resolved soon.

### Response

**Mark Stevens** commented on 11 Jul 2023

This has caused a lot of rework and I'm not sure where the gains are to be had. Hopefully the dev's will consider the amount of work which goes into rectifying breaking changes like this in the future. A 'simple' change like this can cost hours of testing and redeployment across our environments.

## Answer

**Nadezhda Tacheva** answered on 20 Jan 2023

Hello Chris, As of UI for Blazor 4.0. ImageUrl parameter has been removed. You can now pass the desired image through the Icon parameter. Example: [https://blazorrepl.telerik.com/mnOvcYPr31sl6TLf02.](https://blazorrepl.telerik.com/mnOvcYPr31sl6TLf02.) I hope you will find this information useful. Please let us know if any other questions are raised. Regards, Nadezhda Tacheva

### Response

**Arash** commented on 17 Feb 2023

Hi Nadezhda, Thank you for the example you provided. But the thing is for a few custom buttons image, it works despite it take times for developers. In real world with a large-scale application, it's a very time-consuming task to modify and test the whole application. This kind of change is not just renaming a property or method name and it affects all the UI. Regards,

### Response

**Nadezhda Tacheva** commented on 22 Feb 2023

Hi Arash, Thank you for your input! I completely agree with you that in a large-scale application that contains multiple buttons with custom images, this may not be a minor task. Actually, upgrading to a product version that introduces breaking changes may be challenging by itself. Here is why we try to gather the upcoming breaking changes in a single release that takes place only once per year. While such changes are sometimes hard to migrate to, they allow the overall improvement of the product for its future usage.

### Response

**Mark Stevens** commented on 11 Jul 2023

Hi Arash, Can you provide an example of a TelerikMenu using images in a bound datamodel? The menu example uses FontIcon which will not work. public class MenuItem { public int Id { get; set; } public string Text { get; set; } public int? ParentId { get; set; } public bool HasChildren { get; set; } public FontIcon? Icon { get; set; } public string Url { get; set; } public bool Disabled { get; set; } public bool Separator { get; set; } }

### Response

**Mark Stevens** commented on 11 Jul 2023

Hi Arash, I'm using templates so won't require an example thanks.

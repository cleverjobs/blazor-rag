# Error while updating library (progress/kendo-theme-bootstrap) version

## Question

**Mic** asked on 31 May 2022

Hi, I got the following error (in 10805 line of all.css file) while updating @progress/kendo-theme-bootstrap@4.43.0 to @progress/kendo-theme-bootstrap@5.4.1 . Debug in all.scss: What should i do to solve this problem?

### Response

**Michael** commented on 01 Jun 2022

Here's what helped me. Is this solution correct?

### Response

**Nadezhda Tacheva** commented on 03 Jun 2022

Hi Michael, I've reached out to our front-end team to evaluate this case and the solution you've shared. We will get back to you as soon as possible to confirm if this is the best option to proceed with. Thank you for your patience in the meantime!

## Answer

**Teya** answered on 03 Jun 2022

Hello Michael, Can you please share with us the way that you are importing the Kendo Bootstrap theme in your project as well as the way you build the theme? Also, are there any specifics that you use in your setup - variables overrides, etc.? I am asking so that we can try to reproduce the issue at around end and provide you with the best solution. Thank you in advance, Regards, Teya

### Response

**Michael** commented on 14 Jun 2022

I import themes with libman, build them with web-compiler. All variables for themes I take from [https://themebuilder.telerik.com/blazor-ui](https://themebuilder.telerik.com/blazor-ui) (based on bootstrap).

### Response

**Nadezhda Tacheva** commented on 17 Jun 2022

Hi Michael, Thank you for the provided details! This will help our front-end engineers move forward towards resolving the case. The process will require some time for reproduction and testing. We will then get back to you to provide more details on the matter. Thank you once again for your patience!

### Response

**Teya** commented on 23 Jun 2022

Hello Michael, Thank you for the provided information about your setup. I believe that the issue is related to the WebCompiler extension that you are using for compiling the Kendo Sass themes. The original WebCompiler extension was lastly updated more than 5 years ago and most probably does not support the more modern get-function() Sass function. This is why it fails to compile correctly the Sass files. Instead of using WebCompiler, I would rather suggest checking our article on Compiling themes and use a different Sass compiler. I hope this would be helpful.

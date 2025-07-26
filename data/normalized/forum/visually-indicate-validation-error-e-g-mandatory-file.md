# Visually indicate validation error e.g. mandatory file

## Question

**Dea** asked on 21 Apr 2021

Hi all. I am just wondering if anyone has any ideas for making it possible to visually indicate failed validation on an Upload control? To be clear, I have the validation working, it's just that there is no visual clue to the problem - the upload control is not highlighted like other controls are. I looked at the example at [https://github.com/telerik/blazor-ui/tree/master/upload/form-validation](https://github.com/telerik/blazor-ui/tree/master/upload/form-validation) but even on there, you can see the issue - name and email address are highlighted but CV is not. Any thoughts for a workaround? Thanks, Dean

## Answer

**Marin Bratanov** answered on 21 Apr 2021

Hello Dean, There is no built-in validation for file uploads in the framework and so the Telerik component cannot have such an invalid state. What you can do, however, is to set its Class conditionally to a CSS class in your app that you can cascade styles through (say, add a red border to the upload). You can base this condition on the flag that indicates whether its validation passes. If you do that, feel free to open a pull request to add it to the sample, we award such contributions with Telerik points. Regards, Marin Bratanov

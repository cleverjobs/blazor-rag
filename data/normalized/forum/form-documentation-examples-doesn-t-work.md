# Form documentation examples doesn't work

## Question

**Bla** asked on 07 Mar 2022

Hello. I'm wondering why the documentation examples in Form section: Automatic Generated Fields doesn't work. I simply copy and paste the example in a clean Blazor project with Telerik for Blazor 3.0.0 and the compiler can't find the definition for FormEditorType. I don't missing any reference even tried the full namespace that the API documentation indicate and I didn't find any comment that the property is deprecated. Any ideas? Regards. Ludwig.

## Answer

**Nadezhda Tacheva** answered on 08 Mar 2022

Hi Ludwig, We added the ability to customize the automatically generated fields of the Form through the EditorType parameter in the 3.1.0 release of Telerik UI for Blazor. Therefore, you cannot access this functionality using version 3.0.0. Having this in mind, if you now upgrade to 3.1.0, you will be able to use the EditorType attribute to customize the editor fields. We generally recommend always using the latest version of the product. Thus you can benefit from all new components, enhancements and bug fixes we continuously release. I hope this information will help you move forward with your application. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Blazorist** commented on 08 Mar 2022

Thak you Nadezhda for your answer. I feel so silly for not checking the version of the library. One suggestion: Couldn't you keep the documentation of the old versions on the site? In such a way to be able to choose the version of the library with which you are working and thus avoid this type of situation. It does not seem expensive and it would not force to update the version of Telerik permanently so the library version match the documentation. Regards.

### Response

**Svetoslav Dimitrov** commented on 11 Mar 2022

Hello Ludwig, Keeping multiple versions of our documentation is something that we would not like to do, let me provide some additional information on why this is the case: The documentation will become really long and hard to maintain. We have to break changes releases that would include self-contradictory articles in the documentation. Further , we would also encourage our customers to upgrade to the latest version of the Telerik UI for Blazor version. As a general rule, we are commited to supporting the latest version of our product, and thus we would need our documentation to be always in sync with the versions.

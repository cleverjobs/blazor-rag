# Masked Textbox - Allow Insert?

## Question

**Dav** asked on 03 Oct 2023

We are using a masked textbox to allow users to enter a US phone number, formatted as 000-000-0000, so all digits are required. The user is collecting a phone number from someone on a telephone call. Most of the time, the caller provides their phone number area code first, then they give the 7 digit number, so that works great. But sometimes, the caller doesn't think about giving their area code. In that case, the number looks like: 555-555-5, which is not right. Then we have to ask the caller for their area code. If the user clicks before the first 5, and starts typing, they overwrite the existing numbers. We would like it to insert the area code and push everything else to the right. If there are already 10 digits and we just want to change a number, then overwrite. Does that make sense? Is that something that can be done?

## Answer

**Svetoslav Dimitrov** answered on 06 Oct 2023

Hello David, I understand your suggestion to enhance the MaskedTextBox for your particular use case, and it does seem like a reasonable idea. Nonetheless, it's important to consider that implementing this enhancement could potentially disrupt other scenarios where the mask is designed to start with or include specific symbols in predefined locations. With that in mind, I would advise using a TextBox along with custom validation to guarantee the correctness of the phone number input. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**David** commented on 06 Oct 2023

Thanks. That is what we are doing.

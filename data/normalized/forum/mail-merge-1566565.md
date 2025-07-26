# Mail merge

## Question

**Pau** asked on 25 May 2022

Hi Is there any RTF like editor which we can use to create a RTF file with Mail merge field which we can use to create a template that can be used to generare DOCX or PDF files? Eric PS The Editor is missing in the list of Tags

## Answer

**Hristian Stefanov** answered on 30 May 2022

Hi Eric, The desired result seems possible currently with our Editor. The idea is to use a combination between the Editor and the RadFlowDocument from the WordsProcessing. The Editor allows you to convert and export its HTML into plain text, pdf, etc. We have a knowledge base article that shows the Editor exporting its HTML: Convert Editor Value to Plain Text. Use the example from the knowledge base article and replace the plain text exportation with PDF/DOCX. The exportation happens through the RadFlowDocument. Here is an example of RadFlowDocument exporting to PDF and DOCX: RadFlowDocument PDF Export RadFlowDocument DOCX Export Lastly, here is the article for Mail Merge functionality that WordsProcessing also provides: Mail Merge. I hope this helps. If further concerns appear, I would be glad to help. Regards, Hristian Stefanov

### Response

**Paul** commented on 30 May 2022

Hi What if I let the user crate a Word document with merge fields off line, he or she uploads the document and I would only like to mail merge it with a dataset. is this possible? Eric

### Response

**Dimitar** commented on 02 Jun 2022

Hi Eric, Yes, this is possible, after the document is uploaded you will need to perform 3 steps: Import the document with the DocxFormatProvider which will return a RadFlowDocument instance. Perform the mail merge. Export the result document with the provider. Here is an example of this: DocxFormatProvider provider=new DocxFormatProvider();
RadFlowDocument document=provider.Import(File.ReadAllBytes( @"..\..\sampleDoc" ));

RadFlowDocument mailMergeResult=document.MailMerge(mailMergeDataSource);

File.WriteAllBytes( @"..\..\result.docx", provider.Export(mailMergeResult)); Let me know if I can assist you further.

# PDF Viewer - Loading time takes too long

## Question

**Car** asked on 13 Nov 2023

Hello, I'm using PDF Viewer to load a byte[] from my file file info : 28 pages size : 3,4MB It takes almost 20 seconds to load my pdf... theres an option to optimize this? Code: @if (arquivopdf !=null) { <div class="mt-n7"> <TelerikPdfViewer @ref="@PdfViewerRef" Width="100%" Height="800px" Data="arquivopdf"> <PdfViewerToolBar> <PdfViewerToolBarZoomTool /> <PdfViewerToolBarCustomTool> <MudIconButton Icon="@Icons.Material.Filled.Download" Size="Size.Small" Color="Color.Dark" OnClick="BaixarArquivo" Style="@ocultarImprimir" /> </PdfViewerToolBarCustomTool> <PdfViewerToolBarCustomTool> <MudIconButton Icon="@Icons.Material.Filled.MobileScreenShare" Size="Size.Small" Color="Color.Dark" OnClick="()=> AbrirEncaminhar()" Style="@ocultarEncaminhar" /> </PdfViewerToolBarCustomTool> <PdfViewerToolBarCustomTool> <MudIconButton Icon="@Icons.Material.Filled.ArrowBack" Disabled="@disableAnterior" Size="Size.Small" Color="Color.Dark" Style="@ocultarBtnAnterior" OnClick="()=> CarregarAnterior()" /> </PdfViewerToolBarCustomTool> <PdfViewerToolBarCustomTool> <MudIconButton Icon="@Icons.Material.Filled.ArrowForward" Disabled="@disableProximo" Size="Size.Small" Color="Color.Dark" Style="@ocultarBtnProximo" OnClick="()=> CarregarProximo()" /> </PdfViewerToolBarCustomTool> <PdfViewerToolBarCustomTool> <MudIconButton Icon="@Icons.Material.Filled.Close" Size="Size.Small" Color="Color.Dark" OnClick="()=> Cancel()" /> </PdfViewerToolBarCustomTool> </PdfViewerToolBar> </TelerikPdfViewer> </div> } protected override async Task OnInitializedAsync() { _relatorio=await _RelatorioService.ObterRelatorioPorId(Id); arquivopdf=_relatorio.Arquivo; }

## Answer

**Hristian Stefanov** answered on 16 Nov 2023

Hi Carlos, I confirm that we already have an open bug report regarding the described problem with the loading time: PDF Viewer initial document load is very slow. I have voted there on your behalf and raised the priority of this issue. By subscribing to the bug report, you will receive email notifications for any updates on its status. I am sorry for any inconvenience the issue may have caused you. In the interim, if any viable workarounds surface, I will promptly share them at the above-provided link. Regards, Hristian Stefanov Progress Telerik

# AzureAppServiceCLI

Tạo Domain Azure nhanh

- Ở Portal Azure chọn cloudshell ở bên phải thanh tìm kiếm sau đó chọn BASH
- Tải file contact json:
wget https://raw.githubusercontent.com/haku1806/AzureAppServiceCLI/main/AppServiceDomain/contact_info.json -O contact.json

- Chạy lệnh tạo domain theo ý bạn:
az appservice domain create -g your-group --hostname your-domain --contact-info=@'contact.json' --accept-terms

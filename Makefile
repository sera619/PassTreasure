# ---------------------------------------------
# Variables
# ---------------------------------------------

APP_NAME = PassTreasure
VERSION_NUM = $(shell python -c "import config; print(config.VERSION_NUM)")
DIST_DIR = dist/$(APP_NAME)
ZIP_NAME = $(APP_NAME)-$(VERSION_NUM)-WinExe.zip

# ---------------------------------------------
# Targets
# ---------------------------------------------
.PHONY: all clean build package

all: clean build package

clean:
	cls
	@echo Cleaning dist...
	@if exist "./build" rd /s /q build
	@if exist "./dist" rd /s /q dist
	@echo "Done."

fullclean:
	cls
	@echo Cleaning full...
	@if exist "./build" rd /s /q build
	@if exist "./dist" rd /s /q dist
	@if exist "./backup" rd /s /q backup
	@if exist "./data" rd /s /q data
	@echo "Done."

build:
	cls 
	@echo Building with PyInstaller...
	@pyinstaller .\app.spec --noconfirm
	@C:\1Coding\solicus\InstallForge\bin\ifbuilderenvx86.exe
	@echo "Build finished."

package:
	cls
	@echo "📦 Creating ZIP package..."
	@if exist "./package/$(ZIP_NAME)" del /s /q .\package\$(ZIP_NAME)
	@copy .\LICENCE .\dist\PassTreasure
	@cd .\dist\PassTreasure && tar.exe -a -c -f .\$(ZIP_NAME) $(APP_NAME).exe _internal LICENCE
	@move .\dist\PassTreasure\$(ZIP_NAME) .\package
	@echo Package created: $(ZIP_NAME)

release:
	cls
	@echo Start release...
	@gh release create $(VERSION_NUM) .\package\$(ZIP_NAME) .\package\Install-PassTreasure.exe --title "$(APP_NAME) v$(VERSION_NUM)" --notes "Automatic release"
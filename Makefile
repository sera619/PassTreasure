# ---------------------------------------------
# Variables
# ---------------------------------------------

APP_NAME = PassTreasure
VERSION_NUM = $(shell python -c "import config; print(config.VERSION_NUM)")
DIST_DIR = dist/$(APP_NAME)
ZIP_NAME = $(APP_NAME)-$(VERSION_NUM).zip

# ---------------------------------------------
# Targets
# ---------------------------------------------
.PHONY: all clean build package

all: clean build package

clean:
	cls
	@echo "🧹 Cleaning dist..."
	@if exist "./build" rd /s /q build
	@if exist "./dist" rd /s /q dist
	@echo "Done."

fullclean:
	cls
	@echo "🧹 Cleaning full..."
	@if exist "./build" rd /s /q build
	@if exist "./dist" rd /s /q dist
	@if exist "./backup" rd /s /q backup
	@if exist "./data" rd /s /q data
	@echo "Done."

build:
	cls 
	@echo "🔨 Building with PyInstaller..."
	@pyinstaller .\app.spec --noconfirm
	@echo "Build finished."

package:
	cls
	@echo "📦 Creating ZIP package..."
#	@move .\dist\PassTreasure\PassTreasure.exe .
	@cd .\dist\PassTreasure && tar.exe -a -c -f .\$(ZIP_NAME) $(APP_NAME).exe ".\_internal"
	@move .\dist\PassTreasure\$(ZIP_NAME) .\package 
#	@move .\PassTreasure.exe .\dist\PassTreasure
#	@move .\$(ZIP_NAME) .\dist\PassTreasure
	@echo Package created: $(ZIP_NAME)
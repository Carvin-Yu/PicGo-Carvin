# PicGo Image Hosting



**PicGo-Core**

v1.5.7

**PicGo**

v2.4.0-beta.8



# Compile

~~~powershell
git clone https://github.com/Carvin-Yu/PicGo-Carvin.git
cd PicGo-Carvin
cd PicGo-Core
yarn
npm run build

cd ..
cd PicGo
yarn
npm i --force
npm run electron:build

cd dist_electron
cp -r win-unpacked PicGoV1.0.0
zip -r PicGoV1.0.0.zip PicGoV1.0.0/*
~~~


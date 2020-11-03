# gotoeat-map_yamanashi

[農林水産省が実施しているGoToEatキャンペーン](https://gotoeat.maff.go.jp/)の山梨県内加盟飲食店を[OpenStreetMap](https://www.openstreetmap.org)を用いて地図として見られるようにするプロジェクトです。

- https://book000.github.io/gotoeat-map_yamanashi/
- [Go To Eat YAMANASHIキャンペーンサイト](https://www.gotoeat-yamanashi.jp/)

## 仕様

GitHub Actionsにより1時間毎に[加盟飲食店検索ページ](https://www.gotoeat-yamanashi.jp/archives/merchant)の`table.shopTable`をスクレイピングし、「加盟飲食店名」・「飲食店種別」・「住所」・「電話番号」を取得しています。  
また、住所から[Geocoding.jp API](https://www.geocoding.jp/)を使用して緯度・経度を取得し、まとめて[`merchants.json`](https://github.com/book000/gotoeat-map_yamanashi/blob/master/merchants.json)に記録しています。

地図の描画に関しては、[Leaflet](https://leafletjs.com/)から[OpenStreetMap](https://www.openstreetmap.org)を用いて描画しています。

## 注意・免責事項

このプロジェクトを使用したことによって引き起こされた問題に関して開発者は一切の責任を負いません。

## 問い合わせ先

当プロジェクトに関する問い合わせは[Twitter@book000](https://twitter.com/book000)で受け付けます。

## ライセンス

このプロジェクトのライセンスは[MIT License](https://github.com/book000/gotoeat-map_yamanashi/blob/master/LICENSE)です。

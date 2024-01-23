class OpenExchange {

    _baseUrl = process.env["VUE_APP_OPEN_EXCHANGE_BASE_URL"]!;
    _appId = process.env["VUE_APP_OPEN_EXCHANGE_APP_ID"]!;

    // don't need to use composition nor heritage for now because it's kinda light for now
    download(today: string) {
        const url = new URL(`${this._baseUrl}/api/historical/${today}.json`);

        url.searchParams.append('app_id', this._appId);

        return fetch(url.toString(), {
            method: 'GET', headers: {
                'Content-Type': 'application/json'
            }
        });
    }
}

export default new OpenExchange();
import {Rates} from "@/core/rates";

class OpenExchangePy {

    _baseUrl = process.env["VUE_APP_OPEN_EXCHANGE_PY_BASE_URL"]!;


    async download(): Promise<Rates[]> /* local hack, I've more recent libs that get in Conflicts by the usage of generators functions */ {
        let count = 50;
        let more = true;
        const rates: Rates[] = []
        do {
            const url = new URL(`${this._baseUrl}/rates/`);
            url.searchParams.append('next', String(count));
            url.searchParams.append('limit', String(15));
            const response = await fetch(url.toString(), {
                method: 'GET', headers: {
                    'Content-Type': 'application/json'
                }
            });
            if (response.status === 200) {
                const value = await response.json();
                count += value.length;
                more = value.length === 50;
                rates.push(...value);
            }
        } while (more)
        return rates;
    }

    async fromDate(date: string) {
        const url = new URL(`${this._baseUrl}/rates/${date}`);

        const response = await fetch(url.toString(), {
            method: 'GET', headers: {
                'Content-Type': 'application/json'
            }
        });

        if (response.status === 200) {
            return response.json();
        }

        throw new Error(`OpenExchangePy query failed with ${response.status} ! [cause: ${(await response.text())}]`);
    }
}

export default new OpenExchangePy();
import OpenExchange from "@/api/OpenExchange";
import OpenExchangePy from "@/api/OpenExchangePy";
import useEventsBus from "@/core/event-bus";

const {emit} = useEventsBus();

export type PrintedRates = {
    rates: { EUR: string, USD: string, JPY: string, GBP: string }
};

export type Rates = {
    date: string,
    name: string,
    value: string
};

export async function getRates(date: string, {scenario = 1} = {scenario: 1}) {
    if (scenario === 1) {
        return scenario1();
    }

    if (scenario === 2) {
        return scenario2();
    }

    async function scenario1() {
        const response = await OpenExchange.download(date);

        if (response.status === 200) {
            return response.text();
        }
        throw new Error(`OpenExchange query failed with ${response.status} ! [cause: ${(await response.json()).description}]`);
    }

    async function scenario2() {
        const rates: Rates[] = await OpenExchangePy.fromDate(date);
        if (rates.length === 0) {
            return undefined;
        }
        const ratesByDate: { [name: string]: string } = {}
        rates
            .forEach((rate) => {
                console.log(rate);
                ratesByDate[rate.name] = rate.value
            });
        return {rates: ratesByDate};
    }
}

export async function loadAll(prefix: string) {
    const rates = await OpenExchangePy.download();
    const ratesByDate: { [date: string]: { [name: string]: string } } = {};
    console.log(rates);

    rates
        .forEach((rate) => {
            console.log(rate);
            ratesByDate[rate.date] ??= {};
            ratesByDate[rate.date][rate.name] = rate.value
        });

    Object.keys(ratesByDate).forEach((date) => {
        return localStorage.setItem(`${prefix}:${date}`, JSON.stringify({rates: ratesByDate[date]}));
    });

    emit('updated:rates', 'reload')

    return ratesByDate;
}
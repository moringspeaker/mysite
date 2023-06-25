import moment from 'moment';

export function formatDatetime(datetimeString, format) {
    let datetime = moment(datetimeString);
    return datetime.format(format);
}

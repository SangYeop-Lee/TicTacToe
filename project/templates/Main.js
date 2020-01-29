import React, { Component } from 'react';
class Main extends React.Component {

    render() {
        return (
            <div id="contents">
                <a id="diary-url" href="{{ url_for('diary') }}">
                    <div className="grid-item" id="diary">
                        {this.props.diary.map((diary, i) =>
                            <div className="diary-items" key={i}>
                                <div className="diary-contents">{diary}</div>
                            </div>
                        )}
                    </div>
                </a>

                <a id="calendar-url" href="{{ url_for('calendar') }}">
                    <div className="grid-item" id="calendar">
                        {this.calendar()}
                    </div>
                </a>
            </div>
        )
    }

    insertDate() {
        const today = this.props.today;
        var first = new Date(today)
        first.setDate(1)

        var end = new Date(first)
        end.setMonth(end.getMonth()+1)

        if (end.getDay()!==0) {
            end.setDate(end.getDate()+6-end.getDay())
        }
        first.setDate(first.getDate()-first.getDay())

        var table = []
        var date = new Date(first)
        for(; date<=end; ) {
            var children = []
            for (var i = 0; i < 7; i++, date.setDate(date.getDate()+1)) {
                children.push(date.getDate())
            }
            table.push(children)
        }

        return (
            <tbody>

            {table.map((week, i)=>
                <tr key={i}>
                    {week.map((day, j) =>
                        <td key={j}>{day}</td>
                    )}
                </tr>
            )}

            </tbody>
        )
    }

    calendar () {

        const monthNames = ["January", "February", "March", "April", "May", "June", "July", "Augaust", "September", "October", "November", "December"]
        return (
            <table>
                <caption>{monthNames[this.props.today.getMonth()]}</caption>
                <thead>
                    <tr>
                        <td>Sun.</td>
                        <td>Mon.</td>
                        <td>Tue.</td>
                        <td>Wed.</td>
                        <td>Thur.</td>
                        <td>Fri.</td>
                        <td>Sat.</td>
                    </tr>
                </thead>
                {this.insertDate()}
            </table>
        )
    }

}
export default Main;
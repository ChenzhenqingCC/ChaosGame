/**
 * Created by wallace&lily on 2016/2/27.
 */
(function ($) {
    //var Mail = {
    //    create: function (info) {
    //        var mail = {};
    //        mail.render = $('<tr></tr>');
    //        mail.tds = [];
    //        for (var i = 1; i <= 3; i++) {
    //            var td = $('<td></td>').appendTo(mail.render);
    //            mail.tds.push(td)
    //        }
    //
    //        mail.update = function (p_info) {
    //            this.id = p_info.id;
    //            this.server = p_info.server;
    //            this.tds[0].text(mail.server);
    //
    //            this.result = p_info.result;
    //            var state = p_info.state;
    //            this.state = state;
    //
    //            if (state != this.state) {
    //                var td = this.tds[1];
    //                td.empty();
    //
    //                if (state == 'fail') {
    //                    td.append($('<span></span>'.attr({class: 'text-warning'}).text('超时')))
    //                }
    //                else if (state == "error") {
    //                    td.append($('<span></span>'.attr({class: 'text-danger'}).text("错误码:" + self.result)))
    //                }
    //                else if (state == "success") {
    //                    td.append($('<span></span>'.attr({class: 'text-success'}).text("成功")))
    //                }
    //                else if (state == "sending") {
    //                    td.append($('<span></span>'.attr({class: 'text-info'}).text("发送中")))
    //                }
    //
    //                var op_td = this.tds[2]
    //                op_td.empty();
    //                if (state == 'fail' || state == "error") {
    //                    td.append($('<a></a>'.attr({
    //                        class: ["glyphicon", "glyphicon-repeat"].join(' '),
    //                        dataTag: "re_link",
    //                        dataRe: this.id,
    //                        onmouseover: '',
    //                        style: 'cursor: pointer;',
    //                        dataToggle: 'tooltip',
    //                        dataPlacement: 'left',
    //                        title: '在多次点击重发也是安全的，不用担心会重复发邮件'
    //                    }).text("重发")))
    //                }
    //            }
    //
    //        };
    //        return mail
    //    }
    //};
    //
    //var Target = {
    //    create: function (info) {
    //        var target = {};
    //        target.render = $('<tr></tr>');
    //        target.td = $('<td></td>').appendTo(target.render);
    //        target.update = function (p_info) {
    //            this.account = p_info.account
    //            this.td.text(this.account)
    //        };
    //        return target
    //    }
    //};
    //
    //var Acc = {
    //    create: function (info) {
    //        var acc = {};
    //        acc.render = $('<tr></tr>');
    //        acc.tds = [];
    //        for (var i = 1; i <= 3; i++) {
    //            var td = $('<td></td>').appendTo(acc.render);
    //            acc.tds.push(td)
    //        }
    //        acc.update = function (p_info) {
    //            this.tds[0].text(p_info.item_type);
    //            this.tds[1].text(p_info.item_id);
    //            this.tds[2].text(p_info.num);
    //        };
    //        return target
    //    }
    //};
    //
    //
    //var MailGroup = {
    //    create: function (info) {
    //        var group = {};
    //        group.mails = [];
    //        group.accs = [];
    //        group.targets = [];
    //        group.get_mail = function (id) {
    //            for (var mail in this.mails) {
    //                if (mail.id == id) {
    //                    return mail
    //                }
    //            }
    //        };
    //        group.get_acc = function (id) {
    //            for (var acc in this.accs) {
    //                if (acc.id == id) {
    //                    return acc
    //                }
    //            }
    //        };
    //        group.get_target = function (id) {
    //            for (var target in this.targets) {
    //                if (target.id == id) {
    //                    return target
    //                }
    //            }
    //        };
    //
    //
    //        var table_row = $("<tr />", {
    //            "class": "accordion-toggle"
    //        });
    //        this.id = info.id;
    //        for (var i = 1; i <= 7; i++) {
    //            var td = $('<td></td>').appendTo(group.render);
    //            table_row.tds.push(td)
    //        }
    //        table_row.tds[0].append(
    //            $("<a/>", {
    //                href: '#',
    //                dataToggle: 'collapse',
    //                dataTarget: 'child_list' + info.id,
    //                "class": 'fui-eye',
    //                onmouseover: '',
    //                style: 'cursor: pointer;'
    //            })
    //        );
    //
    //        var collapse_row = $("<tr />", {
    //            "class": "hiddenRow",
    //            colspan: 6
    //        });
    //        collapse_row.append(
    //            $("<div/>", {
    //                "class": 'accordian-body collapse',
    //                id: 'child_list'+info.id
    //            })
    //        )
    //
    //        group.update = function (p_info) {
    //            if (this.sended != p_info.sended) {
    //                this.sended = p_info.sended;
    //                table_row.tds[1].empty();
    //                table_row.tds[1].append(
    //                    $("<a/>", {
    //                        href: '#',
    //                        "class": (this.sended) ? 'fui-check-circle' : 'fui-cross-circle',
    //                    }));
    //
    //                table_row.tds[6].empty();
    //                if (!this.sended) {
    //                    table_row.tds[6].append(
    //                        $("<a/>", {
    //                            href: '#',
    //                            dataTag: 'del_link',
    //                            dataDel: p_info.id,
    //                            "class": 'fui-cross',
    //                            onmouseover: '',
    //                            style: 'cursor: pointer;'
    //                        }))
    //                }
    //
    //            }
    //            table_row.tds[2].text(p_info.gm_name);
    //            table_row.tds[3].text(p_info.send_date);
    //
    //            if (this.is_to_whole_accounts != p_info.is_to_whole_accounts) {
    //                this.is_to_whole_accounts = p_info.is_to_whole_accounts;
    //                table_row.tds[4].empty();
    //                table_row.tds[4].append(
    //                    $("<a/>", {
    //                        href: '#',
    //                        "class": (this.is_to_whole_accounts) ? 'fui-check-circle' : 'fui-cross-circle'
    //                    }));
    //            }
    //            if (this.state != p_info.state) {
    //                var state = p_info.state;
    //                this.state = state;
    //                table_row.tds[5].empty();
    //                var state_class = "";
    //                if (state == 'fail') {
    //                    state_class = "fui-alert-circle";
    //                }
    //                else if (state == 'error') {
    //                    state_class = "fui-alert-circle";
    //                }
    //                else if (state == 'success') {
    //                    state_class = "fui-check";
    //                }
    //                else if (state == 'sending') {
    //                    state_class = "fui-upload";
    //                }
    //                table_row.tds[5].append(
    //                    $("<a/>", {
    //                        href: '#',
    //                        dataToggle: 'collapse',
    //                        dataTarget: 'child_list' + info.id,
    //                        onmouseover: '',
    //                        style: 'cursor: pointer;',
    //                        "class": state_class
    //                    }));
    //            }
    //
    //
    //            if (p_info.mails) {
    //                for (var iter in p_info.mails) {
    //                    var mail = this.get_mail(iter.id);
    //                    if (mail) {
    //                        mail.update(iter)
    //                    }
    //                    else {
    //                        mail = Mail.create(iter);
    //                        this.mails.push(mail)
    //
    //                    }
    //                }
    //            }
    //            if (p_info.accs) {
    //                for (var iter_acc in p_info.accs) {
    //                    var acc = this.get_acc(iter_acc.id);
    //                    if (acc) {
    //                        acc.update(iter)
    //                    }
    //                    else {
    //                        acc = Acc.create(iter_acc);
    //                        this.accs.push(acc)
    //                    }
    //                }
    //
    //            }
    //            if (p_info.targets) {
    //                for (var iter_target in p_info.targets) {
    //                    var target = this.get_target(iter_target.id);
    //                    if (target) {
    //                        target.update(iter_target)
    //                    }
    //                    else {
    //                        target = Target.create(iter_target);
    //                        this.targets.push(target)
    //                    }
    //                }
    //            }
    //
    //
    //        };
    //        return group;
    //    }
    //};

    $(function () {

        var delete_mail_id = null
        $("[data-tag='del_link']").click(function (event) {
            event.preventDefault();
            delete_mail_id = $(this).attr("data-del")
            $('#confirmModel').modal()
        })

        $('#confirmModel').on('show.bs.modal', function (event) {
            var modal = $(this)
            modal.find(".btn-primary").click(function (e) {
                window.location.replace('/gamemail_del?mail_group_id=' + delete_mail_id + '&page={{ page.number }}');
            });
        })

        $("[data-tag='re_link']").click(function (event) {
            event.preventDefault();
            var resend_mail_id = $(this).attr("data-re")
            var tr_for_state = $(this).closest('tr')
            var tds = tr_for_state.children('td')
            $(tds[1]).empty().append("<span class='text-info'>发送中</span>")
            $(tds[2]).empty()
            $.ajax({
                url: "/gamemail_resend",
                type: "POST",
                data: {mail_id: resend_mail_id, csrfmiddlewaretoken: csrf_token},
                dataType: 'json',
                success: function (rsp_obj) {
                    $(tds[1]).empty().append(rsp_obj.state);
                    $(tds[2]).empty().append(rsp_obj.op);
                },
                done: function (rsp_obj) {
                    alert(rsp_obj)
                }
            });
        })
    });


})(jQuery);
// const THRESHOLD = { bar: 1.0, '°C': 3, times: Infinity };

const GROUPS = [
  // Nếu có giá trị nào mà không cần phải kiểm tra alarm thì thêm noAlarm: true ở cuối cùng

  {
    label: 'Group A — Pressure & Temperature',
    cards: [
      { title: 'Total Cycle A',       pvKey: 'P1_Number_Test_Times',    svKey: 'P1_CountTimes',         unit: 'times', noAlarm: true},
      { title: 'Pressure A',          pvKey: 'P1_Current_PressureHose', svKey: 'P1_PressureSetting',    unit: 'bar'   },
      { title: 'Temperature A Front', pvKey: 'P1_Current_Temp1',        svKey: 'P1_TemperatureSetting', unit: '°C'    },
      { title: 'Temperature A Mid',   pvKey: 'P1_Current_Temp2',        svKey: 'P1_TemperatureSetting', unit: '°C'    },
      { title: 'Temperature A End',   pvKey: 'P1_Current_Temp3',        svKey: 'P1_TemperatureSetting', unit: '°C'    },
    ]
  },
  {
    label: 'Group B — Pressure & Temperature',
    cards: [
      { title: 'Total Cycle B',       pvKey: 'P2_Number_Test_Times',    svKey: 'P2_CountTimes',         unit: 'times', noAlarm: true},
      { title: 'Pressure B',          pvKey: 'P2_Current_PressureHose', svKey: 'P2_PressureSetting',    unit: 'bar'   },
      { title: 'Temperature B Front', pvKey: 'P2_Current_Temp1',        svKey: 'P2_TemperatureSetting', unit: '°C'    },
      { title: 'Temperature B Mid',   pvKey: 'P2_Current_Temp2',        svKey: 'P2_TemperatureSetting', unit: '°C'    },
      { title: 'Temperature B End',   pvKey: 'P2_Current_Temp3',        svKey: 'P2_TemperatureSetting', unit: '°C'    },
    ]
  },
  {
    label: 'Group C — Pressure & Temperature',
    cards: [
      { title: 'Total Cycle C',       pvKey: 'P3_Number_Test_Times',    svKey: 'P3_CountTimes',         unit: 'times', noAlarm: true},
      { title: 'Pressure C',          pvKey: 'P3_Current_PressureHose', svKey: 'P3_PressureSetting',    unit: 'bar'   },
      { title: 'Temperature C Front', pvKey: 'P3_Current_Temp1',        svKey: 'P3_TemperatureSetting', unit: '°C'    },
      { title: 'Temperature C Mid',   pvKey: 'P3_Current_Temp2',        svKey: 'P3_TemperatureSetting', unit: '°C'    },
      { title: 'Temperature C End',   pvKey: 'P3_Current_Temp3',        svKey: 'P3_TemperatureSetting', unit: '°C'    },
    ]
  },
];

GROUPS.forEach((group, gi) => {
  group.cards.forEach((card, ci) => {
    card._pvId    = `pv_${gi}_${ci}`;
    card._svId    = `sv_${gi}_${ci}`;
    card._deltaId = `delta_${gi}_${ci}`;
    card._cardId  = `card_${gi}_${ci}`;
  });
});

const groupsEl = document.getElementById('groups');

GROUPS.forEach((group, gi) => {
  const labelEl = document.createElement('div');
  labelEl.className = 'group-label';
  labelEl.textContent = group.label;
  groupsEl.appendChild(labelEl);

  const grid = document.createElement('div');
  grid.className = 'grid';

  group.cards.forEach((card, ci) => {
    const el = document.createElement('div');
    el.className = 'card';
    el.id = card._cardId;
    el.innerHTML = `
      <div class="card-title">
        <span>${card.title}</span>
      </div>
      <div class="pv-row">
        <span class="pv-value" id="${card._pvId}">—</span>
        <span class="pv-unit">${card.unit}</span>
        <span class="delta ok" id="${card._deltaId}">—</span>
      </div>
      <div class="sv-row">
        <span class="sv-badge">SV</span>
        <span class="sv-value" id="${card._svId}">—</span>
        <span class="sv-unit">${card.unit}</span>
      </div>`;
    grid.appendChild(el);
  });

  groupsEl.appendChild(grid);
});

const statusEl = document.getElementById('status');
const rawEl    = document.getElementById('raw');
const fmt      = v => isNaN(v) ? '—' : parseFloat(v.toFixed(2));
const fmtInt   = v => isNaN(v) ? '—' : Math.round(v);
const now      = () => new Date().toLocaleTimeString('vi-VN', {hour12: false});

function updateCard(card, pv, sv) {

  if (card.noAlarm) {
    document.getElementById(card._pvId).textContent = fmt(pv);
    document.getElementById(card._svId).textContent = fmt(sv);
    document.getElementById(card._deltaId).textContent = '';
    return false;  // không tính vào alarmCount
  }

  const threshold = sv * 0.10; // Ngưỡng chênh lệch
  const diff      = pv - sv;  // Giá trị chênh lệch
  const absDiff   = Math.abs(diff);
  // const isOke     =
  const isAlarm   = absDiff > threshold; // Nếu giá trị vượt ra khoảng ngưỡng cho phép thì sẽ hiển thị đỏ còn không thì màu xanh
  const isWarn    = absDiff > threshold * 0.6 && !isAlarm; // Nếu giá trị vượt ra khoảng ngưỡng cho phép và trong vùng cảnh báo thì sẽ hiển thị màu vàng
  document.getElementById(card._pvId).textContent = fmt(pv);
  document.getElementById(card._svId).textContent = fmt(sv);

  const pvEl    = document.getElementById(card._pvId);
  const deltaEl = document.getElementById(card._deltaId);
  const cardEl  = document.getElementById(card._cardId);

  // Hiển thị xu hướng tăng giảm của giá trị
  const deltaText = isNaN(diff) ? '—'
    : diff > 0  ? `▴${fmt(absDiff)}`
    : diff < 0  ? `▾${fmt(absDiff)}`
    : '▪ 0';
  deltaEl.textContent = deltaText;

  if (isAlarm) {
    pvEl.className    = 'pv-value alarm';
    deltaEl.className = 'delta alarm';
    cardEl.classList.remove('oke-active');
    cardEl.classList.add('alarm-active');
  } else if (isWarn) {
    pvEl.className    = 'pv-value';
    deltaEl.className = 'delta warn';
    cardEl.classList.remove('alarm-active');
  } else {
    pvEl.className    = 'pv-value';
    deltaEl.className = 'delta ok';
    cardEl.classList.add('oke-active');
  }

  return isAlarm;
}

function updateStats(data) {
  const ca = parseFloat(data['P1_Number_Test_Times'] ?? 'NaN');
  const cb = parseFloat(data['P2_Number_Test_Times'] ?? 'NaN');
  const cc = parseFloat(data['P3_Number_Test_Times'] ?? 'NaN');
  const totalCycles = [ca, cb, cc].filter(v => !isNaN(v)).reduce((a, b) => a + b, 0);
  document.getElementById('st-cycles').textContent     = isNaN(totalCycles) ? '—' : Math.round(totalCycles);
  document.getElementById('st-cycles-sub').textContent = `A:${fmtInt(ca)}  B:${fmtInt(cb)}  C:${fmtInt(cc)}`;

  const ovenPv = parseFloat(data['T0_Current_Temp'] ?? 'NaN');
  const ovenSv = parseFloat(data['T0_TemperatureSetting'] ?? 'NaN');
  document.getElementById('st-oven').textContent    = fmtInt(ovenPv);
  document.getElementById('st-oven-sv').textContent = fmtInt(ovenSv);

  document.getElementById('st-update').textContent     = now();
  document.getElementById('st-update-sub').textContent = 'Live';
}

function updateAlarmStats(alarmCount) {
  const countEl = document.getElementById('st-alarm-count');
  const subEl   = document.getElementById('st-alarm-sub');
  countEl.textContent = alarmCount;
  countEl.style.color = alarmCount > 0 ? '#f85149' : '#3fb950';
  subEl.textContent   = alarmCount > 0 ? `${alarmCount} active` : 'No alarms';
  subEl.className     = alarmCount > 0 ? 'stat-sub warn' : 'stat-sub';
}

function connect() {
  const proto = location.protocol === 'https:' ? 'wss' : 'ws';
  const ws    = new WebSocket(`${proto}://${location.host}/ws`);

  ws.onopen = () => {
    statusEl.textContent = 'Connected';
    statusEl.className   = 'connected';
  };

  ws.onmessage = (e) => {
    const data = JSON.parse(e.data);
    let alarmCount = 0;

    GROUPS.forEach(group => {
      group.cards.forEach(card => {
        const pv = parseFloat(data[card.pvKey] ?? 'NaN');
        const sv = parseFloat(data[card.svKey] ?? 'NaN');
        if (updateCard(card, pv, sv)) alarmCount++;
      });
    });

    updateStats(data);
    updateAlarmStats(alarmCount);
    rawEl.textContent = JSON.stringify(data, null, 2);
  };

  ws.onclose = () => {
    statusEl.textContent = 'Disconnected – retrying...';
    statusEl.className   = '';
    setTimeout(connect, 3000);
  };
}

connect();

(function() {
  const proto = location.protocol === 'https:' ? 'wss' : 'ws';
  const hr    = new WebSocket(`${proto}://${location.host}/hot-reload`);
  hr.onmessage = () => location.reload();
  hr.onclose   = () => {};
})();
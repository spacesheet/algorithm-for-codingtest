use std::ptr;

struct RLC {
    resistance: f64,   // 저항(옴)
    inductance: f64,   // 인덕턴스(헨리)
    capacitance: f64,  // 카패시턴스(패럿)
}

impl RLC {
    fn resonant_frequency(&self) -> f64 {
        // 공진 주파수 (rad/s) = 1/sqrt(LC)
        1.0 / (self.inductance * self.capacitance).sqrt()
    }
}

struct SeriesRLC {
    rlc: RLC,
    ptr: *mut u8,
}

// 닫힌형 Q 계산용 함수 + 그 함수 포인터를 const로 노출 (의도했던 *_ptr 개념 유지)
type QSeriesFn = fn(&RLC) -> f64;
fn series_quality_factor_ptr(rlc: &RLC) -> f64 {
    // Series Q = (1/R) * sqrt(L/C)
    (rlc.inductance / rlc.capacitance).sqrt() / rlc.resistance
}
const SERIES_QUALITY_FACTOR_PTR: QSeriesFn = series_quality_factor_ptr;

impl SeriesRLC {
    fn quality_factor(&self, withOmega: bool) -> f64 {
        if !withOmega {
            // 포인터로 가리킨 닫힌형 Q 사용
            return (SERIES_QUALITY_FACTOR_PTR)(&self.rlc);
        }
        // 선택도(Q) = ω0 L / R
        let series_omega = self.rlc.resonant_frequency();
        series_omega * self.rlc.inductance / self.rlc.resistance
    }
}

type QParallelFn = fn(&RLC) -> f64;
fn parallel_quality_factor_ptr(rlc: &RLC) -> f64 {
    // parrel Q = R * sqrt(C) / sqrt(L)
    rlc.resistance * (rlc.capacitance / rlc.inductance).sqrt()
}
const PARALLEL_QUALITY_FACTOR_PTR: QParallelFn = parallel_quality_factor_ptr;

struct ParallelRLC {
    rlc: RLC,
    ptr: *mut u8,
}

impl ParallelRLC {
    fn quality_factor(&self, withOmega : bool) -> f64 {
        if !withOmega {
            return (PARALLEL_QUALITY_FACTOR_PTR)(&self.rlc);
        }
        // 선택도(Q)
        let parallel_omega = 1.0 / self.rlc.resonant_frequency();
        self.rlc.resistance / parallel_omega * self.rlc.inductance;
    }
}

fn main() {
    // 상수 자기참조/포인터 산술은 불가 → 런타임 초기화로 유지
    let series_circuit: SeriesRLC = SeriesRLC {
        rlc: RLC {
            resistance: 10.0,
            inductance: 0.1,
            capacitance: 0.001,
        },
        ptr: ptr::null_mut(), // 자리만 유지
    };

    let parallel_circuit: ParallelRLC = ParallelRLC {
        rlc: RLC {
            resistance: 10.0,
            inductance: 0.1,
            capacitance: 0.001,
        },
        ptr: ptr::null_mut(), // 자리만 유지
    };

    // 원래 선언을 살리되 초기화 (미사용 경고만 발생)
    let series_factor: fn(&RLC) -> f64 = SERIES_QUALITY_FACTOR_PTR;
    let _ = series_factor; // 사용하지 않으면 경고 억제

    let parallel_factor: fn(&RLC) -> f64 = PARALLEL_QUALITY_FACTOR_PTR;
    _ = parallel_factor; // 사용하지 않으면 경고 억제

    println!(
        "Series Circuit Quality Factor: {}",
        series_circuit.quality_factor(true)
    );
    println!(
        "Series Circuit Quality Factor: {}",
        series_circuit.quality_factor(false)
    );

    println!("Parallel Circuit Quality Factor: {}", parallel_circuit.quality_factor(true));
    println!("Parallel Circuit Quality Factor: {}", parallel_circuit.quality_factor(false));
}

use std::fmt;
use std::str::FromStr;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum CouponStatus {
    USED,
    AVAILABLE,
    EXPIRED,
}

#[derive(Debug, Clone, PartialEq)]
pub struct ParseCouponStatusError {
    pub invalid_value: String,
}

impl fmt::Display for ParseCouponStatusError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "enum 값을 찾을 수 없습니다: '{}'", self.invalid_value)
    }
}

impl std::error::Error for ParseCouponStatusError {}

impl FromStr for CouponStatus {
    type Err = ParseCouponStatusError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s.to_lowercase().as_str() {
            "used" => Ok(CouponStatus::USED),
            "available" => Ok(CouponStatus::AVAILABLE),
            "expired" => Ok(CouponStatus::EXPIRED),
            _ => Err(ParseCouponStatusError {
                invalid_value: s.to_string(),
            }),
        }
    }
}

impl fmt::Display for CouponStatus {

    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let s = match self {
            CouponStatus::USED => "used",
            CouponStatus::AVAILABLE => "available",
            CouponStatus::EXPIRED => "expired",
        };
        write!(f, "{}", s)
    }
}

fn main() {
    println!("=== CouponStatus 테스트 ===");
    
    println!("\n1. 문자열에서 변환 테스트:");
    let test_cases = vec!["used", "AVAILABLE", "expired", "invalid"];
    
    for case in test_cases {
        match CouponStatus::from_str(case) {
            Ok(status) => println!("  '{}' -> {:?}", case, status),
            Err(e) => println!("  '{}' -> 에러: {}", case, e),
        }
    }
    
    // Display 테스트
    println!("\n2. 문자열 변환 테스트:");
    let statuses = vec![CouponStatus::USED, CouponStatus::AVAILABLE, CouponStatus::EXPIRED];
    
    for status in statuses {
        println!("  {:?} -> '{}'", status, status);
    }
    
    // 비교 테스트
    println!("\n3. 비교 테스트:");
    let status1 = CouponStatus::USED;
    let status2 = CouponStatus::USED;
    let status3 = CouponStatus::AVAILABLE;
    
    println!("  {:?} == {:?}: {}", status1, status2, status1 == status2);
    println!("  {:?} == {:?}: {}", status1, status3, status1 == status3);
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_from_str() {
        assert_eq!(CouponStatus::from_str("used").unwrap(), CouponStatus::USED);
        assert_eq!(CouponStatus::from_str("USED").unwrap(), CouponStatus::USED);
        assert_eq!(CouponStatus::from_str("available").unwrap(), CouponStatus::AVAILABLE);
        assert_eq!(CouponStatus::from_str("AVAILABLE").unwrap(), CouponStatus::AVAILABLE);
        assert_eq!(CouponStatus::from_str("expired").unwrap(), CouponStatus::EXPIRED);
        assert_eq!(CouponStatus::from_str("EXPIRED").unwrap(), CouponStatus::EXPIRED);
        
        assert!(CouponStatus::from_str("invalid").is_err());
    }
    
    #[test]
    fn test_display() {
        assert_eq!(format!("{}", CouponStatus::USED), "used");
        assert_eq!(format!("{}", CouponStatus::AVAILABLE), "available");
        assert_eq!(format!("{}", CouponStatus::EXPIRED), "expired");
    }
    
    #[test]
    fn test_debug() {
        assert_eq!(format!("{:?}", CouponStatus::USED), "Used");
    }
    
    #[test]
    fn test_equality() {
        assert_eq!(CouponStatus::USED, CouponStatus::USED);
        assert_ne!(CouponStatus::USED, CouponStatus::AVAILABLE);
    }
    
    #[test]
    fn test_clone() {
        let status = CouponStatus::USED;
        let cloned = status.clone();
        assert_eq!(status, cloned);
    }
}
